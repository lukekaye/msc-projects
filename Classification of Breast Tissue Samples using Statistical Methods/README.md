# Classification of Breast Tissue Samples using Statistical Methods

## Overview 

Within the `mlbench` R package is a dataset `BreastCancer` which concerns characteristics of breast tissue samples
collected from 699 women in Wisconsin using fine needle aspiration cytology. Various cytological characteristics were
measured for each sample on a one to ten scale, and the samples were classified as _benign_ or _malignant_.

Within `code.R` is an analysis that explores the dataset and builds classifiers for the tissue samples, using the
cytological characteristics as predictors. Best Subset Selection for logistic regression, LASSO penalty for logistic
regression and quadratic discriminant analysis methods were all considered, using cross-validation and reasoned
comparison between the techniques.

`report.pdf` is a coherent writeup, detailing the procedure followed for this analysis.

Furthermore, a mathematical problem relating to logistic regression and linear discriminant analysis is disjointly solved
afterwards, in the report.