# HealthInsights

We aim to develop a comprehensive analysis and prediction model for county-level health outcomes using a rich dataset of socioeconomic, demographic, and health indicators. This project will leverage advanced data science techniques to uncover insights into public health trends, disparities, and potential interventions across diverse communities in the United States.

The dataset we propose to use measures data for every county in the United States. It has dozens of potential features measuring various public health and socioeconomic factors. We would like to train a model to predict a major health outcome such as Life Expectancy, Diabetes Cases, Years of Potential Life Lost, or Drug Overdose Deaths on a county-by-county basis, and potentially include statistical inference as well. There are over 600 columns in all, though many of these columns are confidence interval endpoints for a measured statistic, and others are measurements for specific ethnic subgroups. The subgroup data are nowhere near as complete as the overall data, and we do not propose to use those as features to train the model. At present, 	we have narrowed our analysis down to somewhere between 80 and 90 variables. 

Data: https://www.countyhealthrankings.org/health-data
Main Dataset: https://www.countyhealthrankings.org/sites/default/files/media/document/2024_county_health_release_data_-_v1.xlsx

Stakeholders: Federal, State, and Local Health Organizations, Insurance Companies, Social Service Agencies, Pharmaceutical Corporations.

Key Performance Indicators (KPIs): Health outcomes based on socioeconomic and geographic factors. If we end up training a regression model, we will focus on accuracy as a key score for model evaluation. However, our model could end up being inferential rather than predictive, in which case we would be more focused on measures of statistical significance.

