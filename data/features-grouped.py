feature_list = ['Deaths', 'Years of Potential Life Lost Rate', '% Fair or Poor Health', 'Average Number of Physically Unhealthy Days', 
                'Average Number of Mentally Unhealthy Days', '% Low Birthweight', '% Adults Reporting Currently Smoking', 
                '% Adults with Obesity', 'Food Environment Index', '% Physically Inactive','% With Access to Exercise Opportunities',
                '% Excessive Drinking', '% Driving Deaths with Alcohol Involvement', 'Chlamydia Rate', 'Teen Birth Rate','% Uninsured', 
                'Primary Care Physicians Rate', 'Dentist Rate', 'Mental Health Provider Rate', 'Preventable Hospitalization Rate', 
                '% with Annual Mammogram','% Vaccinated', '% Completed High School', '% Some College', '% Unemployed', 
                '% Children in Poverty', 'Income Ratio', '% Children in Single-Parent Households', 'Social Association Rate',  
                'Injury Death Rate', 'Average Daily PM2.5', 'Presence of Water Violation', '% Severe Housing Problems', 
                '% Drive Alone to Work', '% Long Commute - Drives Alone','Life Expectancy', 'Age-Adjusted Death Rate','Child Mortality Rate',
                'Infant Mortality Rate','% Frequent Physical Distress', '% Frequent Mental Distress', '% Adults with Diabetes',  
                'HIV Prevalence Rate','% Food Insecure','% Limited Access to Healthy Foods', 'Drug Overdose Mortality Rate',
                '% Insufficient Sleep', '% Uninsured Adults',  '% Uninsured Children', 'Other Primary Care Provider Rate', 
                'High School Graduation Rate', '% Disconnected Youth','Average Grade Performance', 
                'Average Grade Performance.1', 'Segregation Index',  'School Funding Adequacy', 'Gender Pay Gap','Median Household Income',
                '% Enrolled in Free or Reduced Lunch', 'Segregation Index.1', '% Household Income Required for Child Care Expenses',
                'Child Care Centers per 1,000 Children', 'Homicide Rate', 'Suicide Rate (Age-Adjusted)', 'Firearm Fatalities Rate', 
                'Motor Vehicle Mortality Rate', 'Juvenile Arrest Rate','% Voter Turnout', '% Census Participation','Traffic Volume',
                '% Homeowners',  '% Households with Severe Cost Burden','% Households with Broadband Access','Population', 
                '% Less than 18 Years of Age', '% 65 and Over', '% Black', '% American Indian or Alaska Native','% Asian', 
                '% Native Hawaiian or Other Pacific Islander','% Hispanic', '% Non-Hispanic White','% Not Proficient in English',
                '% Female','% Rural']

features_by_category = {
    "Health Behaviors": [
        "% Adults Reporting Currently Smoking",
        "% Adults with Obesity",
        "% Physically Inactive",
        "% With Access to Exercise Opportunities",
        "% Excessive Drinking",
        "% Driving Deaths with Alcohol Involvement",
        "% Insufficient Sleep" #added
    ],
    "Health Outcomes": [
        "Deaths",
        "Years of Potential Life Lost Rate",
        "Life Expectancy",
        "Age-Adjusted Death Rate", #
        "Suicide Rate (Age-Adjusted)", #
        "Firearm Fatalities Rate", #
        "Motor Vehicle Mortality Rate", #
        "% Fair or Poor Health",
        "Average Number of Physically Unhealthy Days",
        "Average Number of Mentally Unhealthy Days",
        "% Low Birthweight",
        "Chlamydia Rate",
        "Teen Birth Rate",
        "Injury Death Rate",
        "Child Mortality Rate",
        "Infant Mortality Rate",
        "% Frequent Physical Distress",
        "% Frequent Mental Distress",
        "% Adults with Diabetes",
        "HIV Prevalence Rate",
        "Drug Overdose Mortality Rate"
    ],
    "Access to Care": [
        "% Uninsured",
        "% Uninsured Adults",
        "% Uninsured Children",
        "Primary Care Physicians Rate",
        "Dentist Rate",
        "Mental Health Provider Rate",
        "Preventable Hospitalization Rate",
        "Other Primary Care Provider Rate",
        "% with Annual Mammogram",
        "% Vaccinated"
    ],
    "Socio-economic Factors": [
        "% Completed High School",
        "% Some College",
        "% Unemployed",
        "% Children in Poverty",
        "Income Ratio",
        "Juvenile Arrest Rate",
        "% Children in Single-Parent Households",
        "Social Association Rate",
        "% Disconnected Youth",
        "High School Graduation Rate",
        "Average Grade Performance",
        "Average Grade Performance.1",
        "Segregation Index",
        "Segregation Index.1",
        "School Funding Adequacy",
        "Gender Pay Gap",
        "Median Household Income",
        "% Voter Turnout",
        "% Census Participation",
        "% Homeowners",
        "% Enrolled in Free or Reduced Lunch",
        "% Household Income Required for Child Care Expenses",
        "Child Care Centers per 1,000 Children"
    ],
    "Physical Environment": [
        "Food Environment Index",
        "% Food Insecure",
        "% Limited Access to Healthy Foods",
        "Average Daily PM2.5",
        "Presence of Water Violation",
        "% Severe Housing Problems",
        "% Drive Alone to Work",
        "% Long Commute - Drives Alone",
        "% Households with Severe Cost Burden",
        "% Households with Broadband Access",
        "Traffic Volume"
    ],
    "Demographics": [
        "Population",
        "% Less than 18 Years of Age",
        "% 65 and Over",
        "% Black",
        "% American Indian or Alaska Native",
        "% Asian",
        "% Native Hawaiian or Other Pacific Islander",
        "% Hispanic",
        "% Non-Hispanic White",
        "% Not Proficient in English",
        "% Female",
        "% Rural"
    ]
}


### Below is a function for generating lists of features present in the dataset:

def extract_features(df, feature_list):
    return [
    feature for feature in feature_list 
    if feature in df.columns 
]