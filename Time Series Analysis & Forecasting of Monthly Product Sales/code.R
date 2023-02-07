# dlm package for dynamic linear modelling
library(dlm)

# read in project data
filename = 'projectdata.txt'
data = read.table(filename, header = FALSE)
y = data[, 7]

# convert data to time series
y = ts(y, start = c(2011,1), end = c(2020, 12), frequency = 12)

# exploratory plot
par(mfrow = c(2,1))
plot(y, xlab = 'Year', ylab = 'Monthly Sales')
points(y, pch = 21, col = 2, bg = 2)
# overlay lines connecting the minima and maxima points of each season
minima_times = seq(2011.083, 2020.083, 1)
lines(minima_times, y[seq(2, 110, 12)],  col = 'blue')
maxima_times = seq(2011.5, 2020.5, 1)
lines(maxima_times, y[seq(7, 115, 12)],  col = 'blue')

# arima modelling


# acf correlogram
acf(y, lag.max = 40)

# first seasonal differences and plots, d* = 1
y_d12 = diff(y, lag = 12)
plot(y_d12, ylab = 'Seasonally Differenced Data')
acf(y_d12, lag.max = 40)

# first non-seasonal differences and plots, d* = 1, d = 1
y_d12_d = diff(y_d12)
plot(y_d12_d, ylab = 'Seasonally & Non-Seasonally Differenced Data')
acf(y_d12_d, lag.max = 40)

# pacf plot, d* = 1, d = 1
pacf(y_d12_d, lag.max = 40)

# ARIMA(1,1,0)x(0,1,1)_12
model_1 = arima(y, order = c(1,1,0), seasonal = c(0,1,1))
resids = model_1$residuals
plot(resids, ylab = 'Residuals')
acf(resids, lag.max = 40)
pacf(resids, lag.max = 40)
tsdiag(model_1) # ljung-box, use the third plot
shapiro.test(resids)

# overfit models
model_1$loglik
# model fits
model_1a = arima(y, order = c(2,1,0), seasonal = c(0,1,1))
model_1b = arima(y, order = c(1,1,1), seasonal = c(0,1,1))
model_1c = arima(y, order = c(1,1,0), seasonal = c(1,1,1))
model_1d = arima(y, order = c(1,1,0), seasonal = c(0,1,2))
# log likelihoods
model_1a$loglik
model_1b$loglik
model_1c$loglik
model_1d$loglik
# likelihood ratio test statistics
test_stata = 2 * (model_1a$loglik - model_1$loglik)
test_statb = 2 * (model_1b$loglik - model_1$loglik)
test_statc = 2 * (model_1c$loglik - model_1$loglik)
test_statd = 2 * (model_1d$loglik - model_1$loglik)
# p-values for the tests assuming chi-square distribution
1 - pchisq(test_stata, df=1)
1 - pchisq(test_statb, df=1)
1 - pchisq(test_statc, df=1)
1 - pchisq(test_statd, df=1)
  
# underfit models
# model fits
model_1e = arima(y, order = c(0,1,0), seasonal = c(0,1,1))
model_1f = arima(y, order = c(1,1,0), seasonal = c(0,1,0))
# log likelihoods
model_1e$loglik
model_1f$loglik
# likelihood ratio test statistics
test_state = 2 * (model_1$loglik - model_1e$loglik)
test_statf = 2 * (model_1$loglik - model_1f$loglik)
# p-values for the tests assuming chi-square distribution
1 - pchisq(test_state, df=1)
1 - pchisq(test_statf, df=1)

# final model summary
model_1


# regression modelling


# fit regression model with linear trend
# construct data frame
month = rep(factor(month.abb, levels = month.abb), length.out = length(y))
y_lin_df = data.frame(y = y, t = 1:length(y), month = month)
# regression fit
lin_mean_model = lm(y ~., data = y_lin_df)
# fitted values and residuals
lin_fits = lin_mean_model$fitted.values
lin_resids = lin_mean_model$residuals
# model summary
summary(lin_mean_model)

# fit regression model with quadratic trend
# construct data frame
y_qua_df = data.frame(y = y, t = 1:length(y), t_sq = (1:length(y))^2, 
                      month = month)
# regression fit
qua_mean_model = lm(y ~., data = y_qua_df)
# fitted values and residuals
qua_fits = qua_mean_model$fitted.values
qua_resids = qua_mean_model$residuals

# fitted values and residuals plots
# convert fits and resids to ts
lin_fits = ts(lin_fits, start = start(y), end = end(y), 
              frequency = frequency(y))
lin_resids = ts(lin_resids, start = start(y), end = end(y), 
                frequency = frequency(y))
qua_fits = ts(qua_fits, start = start(y), end = end(y), 
              frequency = frequency(y))
qua_resids = ts(qua_resids, start = start(y), end = end(y), 
                frequency = frequency(y))
# plot the data with overlaid fits
plot(y, ylab = 'Monthly Sales', main = 'Linear Trend Fits')
lines(lin_fits, col = 'red')
legend('topleft', c('Data', 'Fitted Values'), col = c('black', 'red'), lty = 1)
plot(y, ylab = 'Monthly Sales', main = 'Quadratic Trend Fits')
lines(qua_fits, col = 'red')
legend('topleft', c('Data', 'Fitted Values'), col = c('black', 'red'), lty = 1)

#aic scores for quadratic and linear trend models, and their difference
c(AIC(lin_mean_model), AIC(qua_mean_model), 
  AIC(lin_mean_model)-AIC(qua_mean_model))

# plot quadratic trend model residuals
plot(qua_resids, ylab = 'Residuals')

# acf and pacf of residuals
acf(qua_resids)
pacf(qua_resids)

# fit zero-mean AR(2) model to residuals, then residual plots
model_1 = arima(qua_resids, order = c(2,0,0), include.mean = FALSE)
plot(model_1$residuals, ylab = 'Residuals')
acf(model_1$residuals)
pacf(model_1$residuals)
tsdiag(model_1) # ljung-box, use the third plot
shapiro.test(model_1$residuals)

# candidate models to replace current
model_1$loglik
# model fits
model_1a = arima(qua_resids, order = c(3,0,0), include.mean = FALSE)
model_1b = arima(qua_resids, order = c(2,0,1), include.mean = FALSE)
model_1c = arima(qua_resids, order = c(1,0,0), include.mean = FALSE)
# log likelihoods
model_1a$loglik
model_1b$loglik
model_1c$loglik
# likelihood ratio test statistics
test_stata = 2 * (model_1a$loglik - model_1$loglik)
test_statb = 2 * (model_1b$loglik - model_1$loglik)
test_statc = 2 * (model_1$loglik - model_1c$loglik)
# p-values for the tests assuming chi-square distribution
1 - pchisq(test_stata, df=1)
1 - pchisq(test_statb, df=1)
1 - pchisq(test_statc, df=1)

# final residual arma model and main model summary
summary(qua_mean_model)
model_1


# dynamic linear modelling


# function to build dlm
build_model = function(params) {
  dlmModPoly(order = 2, dV = exp(params[1]), dW = exp(params[2:3])) +
    dlmModTrig(s = 12, dV = 0, dW = exp(rep(params[4], 11)))
}

# find mles for dlm and check convergence
model_fit = dlmMLE(y, parm = c(0, 0, 0, 0), build = build_model)
model_fit$convergence # should equal 0

# build model for data
model = build_model(model_fit$par)

# view smoothed values alongside data
model_smooth = dlmSmooth(y, model)
model_level = dropFirst(model_smooth$s[, 1])
plot(y, xlab = 'Year', ylab = 'Monthly Sales')
lines(model_level, col = 'red')
legend('topleft', c('Data', "Smoothed Trend"), col=c("black", "red"), lty = 1)

# residual analysis for dlm
model_filter = dlmFilter(y, model)
resids = residuals(model_filter, sd = FALSE)
plot(resids, ylab = 'Residuals')
acf(resids)
pacf(resids)
tsdiag(model_filter) # ljung-box, use the third plot
shapiro.test(resids)

# final dlm summary
str(model) # derive components from this
# trend and seasonal component decomposition
x = cbind(y, dropFirst(model_smooth$s[,1]),
          dropFirst(model_smooth$s[,-(1:2)]) %*% t(model$FF)[-(1:2)])
colnames(x) = c("Sales", "Trend", "Seasonal Effects")
plot(x, type="o", main="Monthly Sales")


# regression model forecasting


# divide the data into a training and test set
train_y = ts(y[1:108], start = c(2011,1), end = c(2019, 12), frequency = 12)
test_y = ts(y[109:120], start = c(2020,1), end = c(2020, 12), frequency = 12)

# fit linear regression model on training set
# construct data frame
month = rep(factor(month.abb, levels = month.abb), length.out = length(train_y))
train_y_df = data.frame(train_y = train_y, t = 1:length(train_y), month = month)
# regression fit
train_y_mean_model = lm(train_y ~., data = train_y_df)
summary(train_y_mean_model)
# residual ARMA fit
resids = train_y_mean_model$residuals
resids = ts(resids, start = start(train_y), end = end(train_y), 
            frequency = frequency(train_y))
train_y_resids_model = arima(resids, order = c(2,0,0), include.mean = FALSE)
train_y_resids_model

# linear forecasts for the test set period
# forecast of the residuals
forecast_resids = predict(train_y_resids_model, n.ahead = 12)
preds_resids = forecast_resids$pred # point forecasts
predvar_resids = forecast_resids$se^2 # forecast variances
# forecasts of the linear and seasonal components
new_month = factor(month.abb, levels = month.abb)
new_y_df = data.frame(t = 109:120, month= new_month)
forecast = predict(train_y_mean_model, new_y_df) # naive point forecasts
preds_naive = ts(forecast, frequency = 12, start = c(2020,1))
# construct overall forecasts
confvar = predict(train_y_mean_model, new_y_df, interval = 'confidence',
                  se.fit = TRUE)$se.fit^2 # mean model confidence int. variances
preds = preds_naive + preds_resids # overall point forecasts
predvar = confvar + predvar_resids # overall forecast variances
lower0.95 = preds - 1.96 * sqrt(predvar) # lower bound at 95%
upper0.95 = preds + 1.96 * sqrt(predvar) # upper bound at 95%
lower0.99 = preds - 2.58 * sqrt(predvar) # lower bound at 99%
upper0.99 = preds + 2.58 * sqrt(predvar) # upper bound at 99%
lower0.999 = preds - 3.29 * sqrt(predvar) # lower bound at 99.9%
upper0.999 = preds + 3.29 * sqrt(predvar) # upper bound at 99.9%

# plot linear point forecasts, forecast prediction intervals, test set
train_y_preds_forecast = ts(preds, start = c(2020,1), frequency = 12)
plot(test_y, xlab = 'Month (2020)', ylab = 'Monthly Sales', xaxt = 'n', 
     ylim = c(300,700), main = 'Linear Trend Model Forecasts')
tsp = attributes(test_y)$tsp
axis(1, at = seq(tsp[1], tsp[2], along = test_y), labels=new_month)
lines(train_y_preds_forecast, col = 'orange')
lines(lower0.95, lty=2, col= 'red')
lines(upper0.95, lty=2, col= 'red')
lines(lower0.99, lty=2, col= 'brown1')
lines(upper0.99, lty=2, col= 'brown1')
lines(lower0.999, lty=2, col= 'brown4')
lines(upper0.999, lty=2, col= 'brown4')
legend("topleft", c('Test Set Data', 'Point Forecasts', 
                    '95% Prediction Intervals', 
                    '99% Prediction Intervals', 
                    '99.9% Prediction Intervals'), 
       col=c('black', "orange", "red", "brown1", "brown4"),
       lty = c(1,1,1,1,1),
       cex = 0.85)

# fit quadratic regression model on training set
# construct data frame
month = rep(factor(month.abb, levels = month.abb), length.out = length(train_y))
qua_train_y_df = data.frame(train_y = train_y, t = 1:length(train_y), 
                            t_sq = (1:length(train_y))^2, month = month)
# regression fit
qua_train_y_mean_model = lm(train_y ~., data = qua_train_y_df)
summary(qua_train_y_mean_model)
# residual ARMA fit
resids = qua_train_y_mean_model$residuals
resids = ts(resids, start = start(train_y), end = end(train_y), 
            frequency = frequency(train_y))
qua_train_y_resids_model = arima(resids, order = c(2,0,0), include.mean = FALSE)
qua_train_y_resids_model

# quadratic forecasts for the test set period
# forecast of the residuals
forecast_resids = predict(qua_train_y_resids_model, n.ahead = 12)
preds_resids = forecast_resids$pred # point forecasts
predvar_resids = forecast_resids$se^2 # forecast variances
# forecasts of the linear and seasonal components
new_month = factor(month.abb, levels = month.abb)
new_y_df = data.frame(t = 109:120, t_sq = (109:120)^2, month= new_month)
forecast = predict(qua_train_y_mean_model, new_y_df) # naive point forecasts
preds_naive = ts(forecast, frequency = 12, start = c(2020,1))
# construct overall forecasts
confvar = predict(qua_train_y_mean_model, new_y_df, interval = 'confidence',
                  se.fit = TRUE)$se.fit^2 # mean model confidence int. variances
preds = preds_naive + preds_resids # overall point forecasts
predvar = confvar + predvar_resids # overall forecast variances
lower0.95 = preds - 1.96 * sqrt(predvar) # lower bound at 95%
upper0.95 = preds + 1.96 * sqrt(predvar) # upper bound at 95%
lower0.99 = preds - 2.58 * sqrt(predvar) # lower bound at 99%
upper0.99 = preds + 2.58 * sqrt(predvar) # upper bound at 99%
lower0.999 = preds - 3.29 * sqrt(predvar) # lower bound at 99.9%
upper0.999 = preds + 3.29 * sqrt(predvar) # upper bound at 99.9%

# plot quadratic point forecasts, forecast prediction intervals, test set
qua_train_y_preds_forecast = ts(preds, start = c(2020,1), frequency = 12)
plot(test_y, xlab = 'Month (2020)', ylab = 'Monthly Sales', xaxt = 'n', 
     ylim = c(300,700), main = 'Quadratic Trend Model Forecasts')
tsp = attributes(test_y)$tsp
axis(1, at = seq(tsp[1], tsp[2], along = test_y), labels=new_month)
lines(qua_train_y_preds_forecast, col = 'orange')
lines(lower0.95, lty=2, col= 'red')
lines(upper0.95, lty=2, col= 'red')
lines(lower0.99, lty=2, col= 'brown1')
lines(upper0.99, lty=2, col= 'brown1')
lines(lower0.999, lty=2, col= 'brown4')
lines(upper0.999, lty=2, col= 'brown4')
legend("topleft", c('Test Set Data', 'Point Forecasts', 
                    '95% Prediction Intervals', 
                    '99% Prediction Intervals', 
                    '99.9% Prediction Intervals'), 
       col=c('black', "orange", "red", "brown1", "brown4"),
       lty = c(1,1,1,1,1),
       cex = 0.85)

# mean absolute percentage error of linear forecasts and observations
(mape = mean(100*abs(as.numeric(test_y) - preds)/as.numeric(test_y)))

# forecasts for the full model
# fit full regression model again
# construct data frame
month = rep(factor(month.abb, levels = month.abb), length.out = length(y))
y_df = data.frame(y = y, t = 1:length(y), t_sq = (1:length(y))^2, month = month)
# regression fit
mean_model = lm(y ~., data = y_df)
# residuals
resids = mean_model$residuals
resids = ts(resids, start = start(y), end = end(y), frequency = frequency(y))
# fit zero-mean AR(2) model
resids_model = arima(resids, order = c(2,0,0), include.mean = FALSE)
# forecast of the residuals
forecast_resids = predict(resids_model, n.ahead = 6)
preds_resids = forecast_resids$pred # point forecasts
predvar_resids = forecast_resids$se^2 # forecast variances
# forecast of the linear and seasonal components
new_month = factor(month.abb[1:6], levels = month.abb[1:6])
new_y_df = data.frame(t = 121:126, t_sq = (121:126)^2, month= new_month)
forecast = predict(mean_model, new_y_df) # naive point forecasts
preds_naive = ts(forecast, frequency = 12, start = c(2021,1))
# construct overall forecasts
confvar = predict(mean_model, new_y_df, interval = 'confidence',
                  se.fit = TRUE)$se.fit^2 # mean model confidence int. variances
preds = preds_naive + preds_resids # overall point forecasts
predvar = confvar + predvar_resids # overall forecast variances
lower = preds - 1.96 * sqrt(predvar) # lower bound at 95%
upper = preds + 1.96 * sqrt(predvar) # upper bound at 95%

# plot point forecasts, forecast prediction intervals for 2021 jan - jun
y_forecast = ts(c(y, upper), start = start(y), frequency = frequency(y))
y_preds = ts(c(y[length(y)], preds), start = end(y), frequency = frequency(y))
plot(y_forecast, ylab = 'Monthly Sales', type = 'n')
lines(y, col = 'black')
lines(y_preds, col = 'red')
lines(lower, lty=2, col= 'orange2')
lines(upper, lty=2, col= 'orange2')
points(ts(y_preds[-1], start = c(2021, 1), frequency = 12), 
       pch = 21, col = 2, bg = 2, cex = 0.5)
legend("topleft", c('Data', 'Point Forecasts', 
                    '95% Prediction Intervals'), 
       col=c('black', "red", "orange2"),
       lty = c(1,1,2),
       cex = 0.9)

# zoomed in version of the above plot
plot(y_forecast, ylab = 'Monthly Sales', type = 'n', xlim = c(2019,2021.5))
lines(y, col = 'black')
lines(y_preds, col = 'red')
lines(lower, lty=2, col= 'orange2')
lines(upper, lty=2, col= 'orange2')
points(ts(y_preds[-1], start = c(2021, 1), frequency = 12), 
       pch = 21, col = 2, bg = 2, cex = 0.5)
legend("bottomright", c('Data', 'Point Forecasts', 
                        '95% Prediction Intervals'), 
       col=c('black', "red", "orange2"),
       lty = c(1,1,2),
       cex = 0.9)