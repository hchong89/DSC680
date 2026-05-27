# Income, Happiness, and Suicide Rate Analysis

## Overview
This project analyzes the relationship between income, happiness, and suicide rates across countries between 2015 and 2017. The objective of the analysis was to explore whether higher-income countries tend to have higher happiness levels and lower suicide rates.

The project combines multiple datasets and applies statistical analysis techniques in R to evaluate correlations and predictive relationships among the variables.

---

## Technologies Used
- R
- ggplot2
- dplyr
- tidyr
- readxl

---

## Data Sources
The analysis combines data from multiple public datasets:

- World Happiness Report
- Income by Country Dataset
- Suicide Rate by Country Dataset

The datasets were merged together using country names and filtered to include only countries available across all datasets.

---

## Project Objectives
- Explore the relationship between national income and happiness
- Analyze whether higher income is associated with lower suicide rates
- Evaluate correlations between happiness and suicide rates
- Compare trends across the years 2015–2017
- Apply statistical modeling techniques to identify significant relationships

---

## Methods
The project included several stages of data preparation and analysis:

### Data Cleaning
- Renamed variables for consistency
- Removed unnecessary columns
- Standardized country names
- Filtered countries shared across all datasets
- Converted character variables into numeric formats

### Exploratory Data Analysis
- Scatterplots comparing:
  - Income vs Happiness
  - Income vs Suicide Rate
- Residual plots
- Q-Q plots for normality assessment

### Statistical Analysis
- Correlation testing
- Linear regression modeling
- Residual analysis
- R-squared evaluation

---

## Key Findings
- A strong positive relationship was found between income and happiness
- Countries with higher income levels generally reported higher happiness scores
- Suicide rates did not demonstrate a strong relationship with income or happiness
- Linear regression models showed moderate predictive ability for happiness using income data

---

## Results
The analysis found:

- Correlation between income and happiness:
  - Approximately 0.72
- Weak correlation between suicide rate and income
- Weak correlation between suicide rate and happiness

The regression analysis suggested that income was a meaningful predictor of happiness, while suicide rates were not strongly explained by the variables included in the model.

---

## Limitations
- Happiness is subjective and difficult to measure objectively
- Country-level analysis may hide regional differences within countries
- Additional economic and social variables could improve predictive performance
- Data availability limited the analysis to selected years

---

## Files Included
- `Income happiness and suicidal rate.Rmd` — Full R Markdown analysis

---

## Future Improvements
Possible future extensions of this project include:
- Adding GDP and unemployment variables
- Expanding analysis to more years
- Applying machine learning regression models
- Performing regional or state-level analysis
- Building interactive dashboards for visualization

```
