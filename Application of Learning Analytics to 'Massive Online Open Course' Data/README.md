# Application of Learning Analytics to 'Massive Online Open Course' Data

## Overview 

This directory contains an analysis on data derived from a free course provided by a university, relating to the subject
of safety while using technology and the internet. The report details insights into how a stakeholder interested in the
course may improve engagement with future students. Use of good data mining practice, outlined by the CRISP-DM methodology,
is considered for this purpose, including attention to reproducibility. The analysis is explained in
detail in a 20-page report that can be found in the `reports` subdirectory, thus explanation of the project is minimised
here.

To simply view the report and its results in `.pdf` format, no libraries need to be installed; installation of
libraries only applies if you wish to reproduce the analysis itself.

## Directory Content & How to Run the Analysis

The following R libraries are required for the analysis:
- `gridExtra`
- `AER`
- `countreg`
- `tidyverse`
- `nonnest2`

`countreg` must be installed first by running `install.packages("countreg", repos = "http://R-Forge.R-project.org")` within R.
Afterwards, the remaining libraries will be installed automatically when the analysis is run.

After `countreg` is installed, the main analysis can be viewed by entering the `reports` subdirectory and running `main_report.Rmd`, an
RMarkdown file that details the content of the analysis. This RMarkdown file also contains excerpts of code that serve as part of the
analysis. Alternatively, the main analysis can be viewed in `.pdf` form within this same subdirectory under `main_report.pdf`.

This RMarkdown file, within the body of its content, details fully how the analysis works with the subdirectories within this directory,
however we briefly outline it here too.
- `cache`: stores cached versions of all of the raw data files and partially or fully preprocessed data, for faster loading with R
- `config`: stores the configuration file for this analysis, the load order of the libraries within this file should not be changed
- `data`: the raw data files that were used for the analysis
- `munge`: R scripts that preprocess the data into a form to be used within the main analyses
- `reports`: contains the written report for the analysis in `.pdf` and `.Rmd` format
- `src`: contains most, but not all, of the code used within the main analyses of the report: plots, modelling, etc


In short:
- Install `countreg` manually by running `install.packages("countreg", repos = "http://R-Forge.R-project.org")` within R
- Run `main_report.rmd` within `reports` to view the analysis and its results
- View the `.R` files within `munge` and `src` to see additional code used within the analysis

You may find you need to set your R working directory to this directory if the analysis or `ProjectTemplate` doesn't load properly.

If you wish to generate the `.pdf` main report file again using the RMarkdown file, you will need an installation of LaTeX on your system. A
simple solution for this can be reached by running `install.packages('tinytex')` then `tinytex::install_tinytex()` within R.
