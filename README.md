# Health Insights

A project completed for the Fall 2024 Data Science Course at the Erdos Institute.

**Team Members:** <br>
[Leyda Almodóvar](https://github.com/lalmodovarvel) <br>
[Neal Edgren](https://github.com/nedgren) <br>
[Chiara Mattamira](https://github.com/cmattamira) <br>
[Shravan Patankar](https://github.com/vsop-shravan) <br>

## Project Description 

### Project Overview
We developed a comprehensive analysis for the risk of diabetes at a county-level using a rich dataset of socioeconomic, demographic, and health indicators. We obtained our dataset from County Health Rankings & Roadmaps. Specifically, our objectives are to:
- Identify key risk predictors for diabetes in the US
- Provide insights to help make informed policy decisions
- Understand which populations are at risk at a local level

Stakeholders:  Federal, State, and Local Health Organizations, Insurance Companies, Social Service Agencies, Pharmaceutical Corporations.

### Modeling approach: 
We split the data into 80% training set and 20% testing set. 20% of the training set was reserved as a validation set. After doing some exploratory analysis, we ran some baseline models (mean model, random sampling) on all the features and then we compared linear regression, random forest, and XGBoost. Since XGBoost performed significantly better, we performed cross-validation for this model and tuned hyperparameters. 

We then looked at several models using XGBoost: Full model (includes all 48 features), Health behaviors only, Socioeconomic only, Demographic only, Physical Environment only, Access to Care only.


### Results
For the full model, we found that the percentage of physically inactive people was the most important feature, followed by percentage of children in poverty, and percentage of people who completed high school in a given county. The RMSE for the full model is 0.31.

We also looked at importance by feature group, calculated the RMSE for each, and found that the top features by group are as follows:
- Health behaviors:
  - Top features: % physically inactive, % insufficient sleep, % adults with obesity.
  - RMSE: 0.52 
- Socioeconomic factors:
  - Top features: % children in poverty, % completed high school, % children in single-parent households
  - RMSE: 0.72 
- Demographics:
  - Top features: % hispanic non-white, % black, % asian
  - RMSE: 1.02 
- Physical environment:
  - Top features: % food insecure, % households with broadband access, food environment index
  - RMSE: 1.34 
- Access to care:
  - Top features:% uninsured, % with annual mammograms, % uninsured children
  - RMSE: 1.74 

We compared the prevalence of diabetes between counties with low median income and counties with high median income. We found that demographic features are more predictive for low-income counties, while health behavior features are more predictive for high-income counties. There were also noticeable differences in socioeconomic features.

We also split the data by percentage of non-White and found that for counties below the median income, socioeconomic factors were more important and for counties above the median, health behaviors were more prevalent highlighting the need for tailored interventions that address both health behaviors and socio-economic challenges specific to each racial and income group.

We concluded that diabetes prevalence is not only predicted by health behaviors, as it can be expected but also by socioeconomic factors, with the latter ones being especially important in counties with lower household income.

### Future work
A more in-depth analysis of a specific state or geographical region, making a more inferential model, and further reducing our feature list 

## Dependencies
 XGBoost, Scikit-Learn, Pandas, Numpy, Matplotlib, Seaborn

## Data Access
We used the 2024 County Health Release National Data provided by County Health Rankings & Roadmaps (CHR&R), found at [here](https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation).

## Folder organization and summary

Data
- Data-reduced: Cleaned data set
- Data-reduced-test: Test set of the clean data
- Data-reduced-train: Train set of the clean data
- Features-grouped: List of all features and the groups they belong to (health, socioeconomics, environmental, access to care, demographic)
- Pre-cleaning data sets can also be found here

Exploration
- Exploratory Data Analaysis and plot generation on the entire clean data set
- Exploratory Data Analaysis and plot generation for each feature group

Modeling
- Initial comparison among models
- A more in depth evaluation of XGB & parameter tuning
- Feature importance on all features and on each feature group
- Feature importance on data set split by median of median household income
- Feature importance on data set split by median of % non-hispanic white

Output files
- Final results from models and EDA

### Contact
To further discuss this project or use associate code feel free to contact us: <br>
Leyda Almodóvar - leyda.av@gmail.com <br>
Neal Edgren - n.edgren@gmail.com <br>
Chiara Mattamira - cmattami@vols.utk.edu <br>
Shravan Patankar - shravan.patankar@gmail.com <br>




