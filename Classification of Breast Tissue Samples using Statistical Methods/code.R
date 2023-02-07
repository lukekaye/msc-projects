library(mlbench)
library(bestglm)
library(glmnet)
library(MASS)
data(BreastCancer)

dim(BreastCancer)
head(BreastCancer)



# data cleaning


# convert cytological characteristics to quantitative variables
BreastCancer[, 2:10] = lapply(BreastCancer[, 2:10], as.numeric)
# check conversion has been applied successfully
lapply(BreastCancer, class)
# remove rows containing missing values
BreastCancer = na.omit(BreastCancer)



# exploratory data analysis


# count of each response factor
table(BreastCancer$Class)

# scatterplot matrix of predictors, coloured by response factor, noise added
pairs(lapply(BreastCancer[, 2:10], jitter), col = BreastCancer[, 11])

# compute sample mean vector of predictors
colMeans(BreastCancer[, 2:10])
# compute sample variances of predictors
diag(var(BreastCancer[, 2:10]))
# compute sample correlation matrix of predictors
cor(BreastCancer[, 2:10])



# classification modelling


# standardise data
BreastCancer[, 2:10] = scale(BreastCancer[, 2:10])

# code Class as binary
BreastCancer[, 11] = as.numeric(BreastCancer[, 11])-1

# ensure reproducibility and fairness in model comparison
set.seed(1)

# cross validation folds, used for all models
fold_index = sample(rep(1:10, length = 683)) # n = 683


# non-regularised logistic regression with bss


# bss algorithm on 9 predictors
bss_fit = bestglm(BreastCancer[, 2:11], family = binomial)
bss_fit$Subsets

# compute test error for BSS models

# primary function, uses k-fold validation to find misclassification probability for a model
reg_cv = function(X1, y, fold_ind) {
  Xy = data.frame(X1, y=y) # get data frame formed of predictors and response
  nfolds = max(fold_ind) # get total number of folds
  if(!all.equal(sort(unique(fold_ind)), 1:nfolds)) stop("Invalid fold partition.")
  cv_errors = numeric(nfolds) # empty vector of cv errors
  for(fold in 1:nfolds) {
    tmp_fit = glm(y ~ ., data=Xy[fold_ind!=fold,], family = 'binomial') # fit predictive model
    yhat = predict(tmp_fit, Xy[fold_ind==fold,], type = 'response') # get predicted probs
    yhat_class = round(yhat) # round predicted probs to 1 or 0, i.e. get their classification
    yobs = y[fold_ind==fold] # find the actual classifications in the data set
    cv_errors[fold] = 1 - mean(yobs == yhat_class) # get misclassification probability overall
  }
  fold_sizes = numeric(nfolds)
  for(fold in 1:nfolds) fold_sizes[fold] = length(which(fold_ind==fold))
  test_error = weighted.mean(cv_errors, w=fold_sizes) # weighted by fold sizes, getting overall error
  return(test_error)
}

# pass each BSS model into the above primary function, returning error for each
reg_bss_cv = function(X1, y, best_models, fold_index) {
  p = ncol(X1)
  test_errors = numeric(p)
  for(k in 1:p) { # pass each candidate model into the above function
    test_errors[k] = reg_cv(X1[,best_models[k,]], y, fold_index)
  }
  return(test_errors)
}

# use above functions to return error of each BSS model
bss_err = reg_bss_cv(BreastCancer[, 2:10], BreastCancer[, 11], 
                     as.matrix(bss_fit$Subsets[-1,2:10]), fold_index)

# identify lowest test error model and its error
best_bss_fit_err = min(bss_err)
c(which.min(bss_err), best_bss_fit_err)

# view model with lowest error
bss_fit$Subsets[6, ] # since this table starts from NULL model
best_bss_fit = glm(Class ~ .-Cell.size-Cell.shape-Epith.c.size-Mitoses, data = BreastCancer[, 2:11], family = 'binomial')
summary(best_bss_fit)


# regularised logistic regression with lasso


# grid of values for tuning parameter
grid = 10^seq(5, -3, length = 100)
# cross validated lasso regression fit for each tuning parameter
lasso_cv_fit =cv.glmnet(as.matrix(BreastCancer[,2:10]),BreastCancer[,11],
                        family='binomial',alpha=1,standardize =FALSE,
                        lambda = grid, type.measure = 'class', foldid = fold_index)

# extract LASSO penalty with smallest misclassification probability, and corresponding probability
lambda_min = lasso_cv_fit$lambda.min # LASSO penalty with smallest misclassification probability
lasso_fit_err = lasso_cv_fit$cvm[which(lasso_cv_fit$lambda == lasso_cv_fit$lambda.min)]
c(lambda_min, lasso_fit_err)

# fit lasso model with penalty that minimises misclassification probability
lasso_fit = glmnet(as.matrix(BreastCancer[,2:10]), BreastCancer[,11],
                   family='binomial',alpha=1,standardize=FALSE,lambda = lambda_min)
coef(lasso_fit)
# for comparison, fit and summarise full non-regularised logistic model
lr_fit_full = glm(Class~., data = BreastCancer[, 2:11], family = 'binomial')
summary(lr_fit_full)


# discriminant analysis


# derive and plot first two principle components of data

pca = prcomp(BreastCancer[, 2:10]) # pca of predictors
summary(pca) # find variance explained by first 2 predictors
# Plot the first PC against the second PC with colours and characters in 'Class'
plot(pca$x[,1], pca$x[,2], xlab='PC1', ylab='PC2', col= BreastCancer$Class+1, pch= BreastCancer$Class+1)
legend(x = 'topright', legend = c('Benign','Malignant'), col= c('black','red'), pch = c(1,2))

# find qda model with lowest test error, considering all predictor combinations
best_qda_fit_error = 1 # initialise best test error as maximum possible value
# loop over all length i predictor models
for(i in 1:9) {
  # get all combinations of i predictors, including their data
  i_predictor_combos = combn(BreastCancer[,2:10], i, simplify=FALSE)
  # loop over all j predictor combos of length i
  for(j in 1:length(i_predictor_combos)) {
    model_test_error = 0 # initialise jth model test error
    confusion = integer(length(fold_index)) # initialise empty confusion vector
    # perform cross validation on jth predictor model, using k as the test set
    for(k in 1:10){
      # fit a qda on data with fold_index != k
      qda_cv_fit = qda(x = as.matrix(as.data.frame(i_predictor_combos[j])[fold_index != k, ]), 
                       grouping = BreastCancer[fold_index != k, 11])
      # compute fitted values on data with fold_index == k
      qda_cv_test = predict(qda_cv_fit, as.matrix(as.data.frame(i_predictor_combos[j])[fold_index == k, ]))
      # compute test error for this fold
      k_test_error = 1 - mean(BreastCancer$Class[fold_index == k] == qda_cv_test$class)
      # compute average test error for j across folds, weighted by size of fold
      model_test_error = model_test_error + k_test_error*sum(fold_index==k)/683
      # add classification types to confusion vector, replacing empty values
      confusion[which(fold_index==k,arr.ind=TRUE)] = qda_cv_test$class
    }
    # check if test error of model is superior to current best
    if(model_test_error < best_qda_fit_error) {
      # replace best test error with new best
      best_qda_fit_error = model_test_error
      # record lowest test error qda fit
      best_qda_fit = qda_cv_fit
      # record lowest test error qda confusion vector
      best_qda_confusion = factor(confusion-1)
    }
  }
}
# identify lowest test error model predictors and test error
c(colnames(best_qda_fit$means), best_qda_fit_error)

# fit lowest classification error qda model and summarise
qda_fit = qda(Class ~ Cl.thickness + Cell.shape + Epith.c.size + Bare.nuclei, data = BreastCancer[, 2:11])
qda_fit



# final classification model summaries


# confusion matrix of cv qda model
(confusion = table(Observed=BreastCancer[, 11], Predicted = best_qda_confusion))

# summary of qda model
qda_fit