# msc-projects
A repository containing coursework completed over the course of my MSc in Data Science.

Each project is described below by a narrative of the provided data, its objective and any methods used.

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
  
## Big Data Analytics for Relational & Graph Data on New York Taxi Trips

Data on taxi trips having previously taken place in New York were provided, in both relational and graph format. The tasks for each format of data were disjoint; they are therefore introduced separately.

### Relational Format Taxi Trips Data

Separate datasets on the taxi trips themselves and the geographic zones within New York were given, within a relational database. For the taxi trips, datasets of various sizes were provided, from roughly 3,000,000 observations up to 130,000,000 observations. Additionally, for each dataset size, the data was given in both `parquet` and `delta` format. The task was to clean the data, then perform join operations and various transformations on the columns, and finally display aggregations relating to the data. The task was to be performed using distributed computation, thus designing a pipeline to conduct these operations that exploited the parallelism of this distributed framework was highly important. Finally, pipeline execution times for the different dataset sizes and formats were to be evaluated, to assess the parallelism of this created preprocessing and analysis pipeline.

### Graph Format Taxi Trips Data

A single dataset on the graph structure of New York was given, with associated information on taxi trips embedded into the edges of the graph structure, within a graph database. The tasks were, sequentially, to locate any self-pointing edges or isolated nodes (that is, nodes that only had trips with itself as both the origin and destination), to perform community detection to identify clusters of strongly connected nodes, to perform centrality analysis to quantify the hub-like tendency of each node, and finally to find the highest centrality score nodes within each detected community. The results for each step were individually visualised through a map of the New York taxi zones.

| **Languages/Applications**   | **Major Libraries**                                     |
|------------------------------|---------------------------------------------------------|
| Apache Spark<br/>Databricks<br/>Neo4j<br/>Cypher Query Language<br/>Python            | PySpark<br/> Neo4j Graph Data Science library |

## Application of Learning Analytics to 'Massive Online Open Course' Data

Data from seven runs of a 'massive online open course' were given. Information on students, course engagement and the course itself were available. The task was unrestricted in nature: to gather any insights that may be useful to a provider of a course alike the one described in the data, while completing two cycles of CRISP-DM i.e. the 'Cross-industry standard process for data mining'. The dataset was unedited and inherently noisy; there was therefore a strong emphasis placed on proper exploration and preprocessing.

| **Languages/Applications**   | **Major Libraries**                                     |
|------------------------------|---------------------------------------------------------|
| R<br/>R Markdown            | ProjectTemplate<br/> ggplot2<br/> dplyr |

## Time Series Analysis & Forecasting of Monthly Product Sales

A time series was provided, intended to represent monthly sales of an unspecified product over ten years. The task given was to fit a variety of statistical models to the data and forecast for a period of six months beyond the time series, selecting a final model to do so. Two mathematical questions in time series theory were given to solve.

| **Languages/Applications**   | **Major Libraries** |
|------------------------------|---------------------|
| R                            | dlm                 |

## Classification of Breast Tissue Samples using Statistical Methods

Data concerning cytological characteristics of breast tissue samples collected from women were provided. Each sample had additionally been labelled with whether it was cancerous or not, as _benign_ or _malignant_. The task was to build multiple classifiers for the data, with careful use of cross-validation to contrast the fitted classifiers. A mathematical question relating to logistic regression and linear discriminant analysis was given to solve.

| **Languages/Applications** | **Major Libraries**                |
|----------------------------|------------------------------------|
| R                          | bestglm<br/> glmnet<br/> MASS<br/> |

## Bayesian Analysis of Cross Country Race Times

Data concerning race times, and various other characteristics, relating to a cross country racing league were provided. The task was to utilise Bayesian, as opposed to frequentist, methods to perform inference on the data, attempting to explain the variation in race times by using the other variables within the dataset. Statistical modelling was conducted using Markov chain Monte Carlo simulation, with the validity of each model evaluated using various diagnostics and reasoned comparison used to select a final model.

| **Languages/Applications** | **Major Libraries**                |
|----------------------------|------------------------------------|
| R<br/>JAGS                          | rjags<br/>coda|

## Visualisation of Epidemic Data

Data concerning the results of simulations of an airborne disease outbreak were given. The simulation modelled the outbreak area as a grid of cells, and the output data for each simulation contained information such as cell population, infected count and various uncertainty statistics. The task was to visualise the uncertainty and impact of the outbreak, firstly across a single simulation and then generalising to an arbitrary number of simulations, through the use of interactive dashboards.

| **Languages/Applications** | **Major Libraries** |
|----------------------------|---------------------|
| Power BI                   | _N/A_              |

## Stock Management & Billing Application

As an exercise in software engineering, there was no dataset tied to this project. The task was to design an application that could be used to manage an inventory and produce receipts corresponding to purchases of that inventory. The use of good programming practice was evaluated, including appropriate use of object orientation, unit testing, exception handling and clear code documentation and naming. A Markdown file was required to be produced alongside the application.

| **Languages/Applications** | **Major Libraries**       |
|----------------------------|---------------------------|
| Python<br/> Markdown       | abc<br/> unittest<br/> os |

## High-Level Business Strategy for Implementing Robots in Surgical Procedures

This project entailed detailing how a business could implement a data science solution to improve some facet of their operation, written up as a report and communicated through a presentation. Working as a group of eleven people, the task was to invent a business in a given industry, a problem they were facing that they needed to solve, and how that problem could be solved using data-driven methodology. The solution presented was at a high-level, describing how a data science consultancy could quantitatively evaluate how a healthcare company could stratify an implementation of robots in surgical procedures at their hospitals, for economic and social gain. Emphasis was placed on deriving a solution that addressed the context of the problem and the needs of the business.

| **Languages/Applications** | **Major Libraries**       |
|----------------------------|---------------------------|
| _N/A_       | _N/A_ |
