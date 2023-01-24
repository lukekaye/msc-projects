# msc-projects
A repository containing coursework completed over the course of my MSc in Data Science.

Each project is described below by a narrative of the provided data, its objective and any methods used.

Most of the projects processed a given dataset in some way. Due to licencing issues around distributing datasets, the datasets themselves have been omitted in every case.

As I am still studying the course, this repository is unfinished and will be updated as projects are completed.

## Machine Learning Analyses of Twitter & Weather Data

The analyses for these datasets were disjoint; they are therefore introduced separately.

### Sentiment Analysis of Twitter Data

A dataset was given of approximately 15,000 Tweets relating to airlines. Each Tweet was classed as either _positive_, _neutral_, or _negative_. The task was to build and train a sentiment classifier with as high an F1-score as possible, while carrying out appropriate exploratory analysis, preprocessing methods and evaluation/comparison of fitted machine learning models.

### Forecasting for a Weather Time Series

A time series of minutely data spanning approximately 13 months was given. It contained 8 different features: datetime, six weather features and a count feature. The task was, for each of the weather features, to forecast 5, 10, 15, 30, 60, 120, 360 and 720 minutes beyond the time series, again carrying out appropriate exploratory analysis, preprocessing methods and evaluation/comparison of fitted machine learning models.
  
| **Languages/Applications**   | **Major Libraries**                                                                                                                                                                     |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Python<br/>Jupyter Notebook  | TensorFlow<br/> scikit-learn<br/> scikit-optimize<br/> imbalanced-learn<br/> XGBoost<br/> Transformers<br/> NLTK<br/> SHAP<br/> pandas<br/> pandas-profiling<br/> matplotlib<br/> NumPy |
  
## Application of Learning Analytics to 'Massive Online Open Course' Data

Data from seven runs of a 'massive online open course' were given. Information on students, course engagement and the course itself were available. The task was unrestricted in nature: to gather any insights that may be useful to a provider of a course alike the one described in the data, while completing two cycles of CRISP-DM i.e. the 'Cross-industry standard process for data mining'. The dataset was unedited and inherently noisy; there was therefore a strong emphasis placed on proper exploration and preprocessing. The production of a short recorded presentation describing the analysis was also required.

| **Languages/Applications**   | **Major Libraries**                                     |
|------------------------------|---------------------------------------------------------|
| R<br/>R Markdown            | ProjectTemplate<br/> ggplot2<br/> dplyr |

## Time Series Analysis & Forecasting of Monthly Product Sales

A time series was provided, intended to represent monthly sales of an unspecified product over ten years. The task given was to fit a variety of statistical models to the data and forecast for a period of six months beyond the time series, selecting a final model to do so. The production of a short recorded presentation describing the analysis was also required. Two mathematical questions in time series theory were given to solve.

| **Languages/Applications**   | **Major Libraries** |
|------------------------------|---------------------|
| R                            | dlm                 |

## Classification of Breast Tissue Samples using Statistical Methods

Data concerning cytological characteristics of breast tissue samples collected from women were provided. Each sample had additionally been labelled with whether it was cancerous or not, as _benign_ or _malignant_. The task was to build multiple classifiers for the data, with careful use of cross-validation to contrast the fitted classifiers. The production of a short recorded presentation describing the analysis was also required. A mathematical question relating to logistic regression and linear discriminant analysis was given to solve.

| **Languages/Applications** | **Major Libraries**                |
|----------------------------|------------------------------------|
| R                          | bestglm<br/> glmnet<br/> MASS<br/> |

## Stock Management & Billing Application

As an exercise in software engineering, there was no dataset tied to this project. The task was to design an application that could be used to manage an inventory and produce receipts corresponding to purchases of that inventory. The use of good programming practice was evaluated, including appropriate use of object orientation, unit testing, exception handling and clear code documentation and naming. A Markdown file was required to be produced alongside the application.

| **Languages/Applications** | **Major Libraries**       |
|----------------------------|---------------------------|
| Python<br/> Markdown       | abc<br/> unittest<br/> os |

## Visualisation of Epidemic Data

Data concerning the results of simulations of an airborne disease outbreak were given. 
