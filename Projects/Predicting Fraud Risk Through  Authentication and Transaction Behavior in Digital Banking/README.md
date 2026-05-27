# Predicting Fraud Risk Through Authentication and Transaction Behavior in Digital Banking

## Project Overview

This project analyzes how authentication methods, transaction behavior, and digital activity patterns relate to fraudulent banking transactions. The goal of the project is to better understand which behavioral and authentication-related variables are associated with fraud risk in digital banking systems.

Using machine learning techniques, this project explores whether variables such as login attempts, suspicious IP indicators, transaction velocity scores, and anomaly scores can help predict fraudulent transactions. The project also compares multiple machine learning models to evaluate fraud detection performance.

---

## Business Problem

As online and mobile banking continue to grow, financial institutions face increasing risks related to digital fraud, account takeovers, unauthorized transactions, and suspicious login activity. Banks must balance strong fraud prevention systems while maintaining a positive customer experience.

This project explores how behavioral analytics and authentication-related variables may help improve fraud detection and transaction monitoring within digital banking environments.

---

## Dataset

Dataset Source:
- Kaggle – Banking Fraud Detection & Risk Analytics Dataset

The dataset contains approximately 10,000 banking transaction records and includes:
- authentication type
- login attempts
- suspicious IP indicators
- transaction velocity scores
- anomaly scores
- device risk scores
- international transaction flags
- session duration
- payment channels
- fraud indicators

---

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost

---

## Project Workflow

### 1. Data Cleaning and Preprocessing
- Checked for missing values
- Removed duplicate records
- Encoded categorical variables
- Prepared data for modeling

### 2. Exploratory Data Analysis (EDA)
- Fraud distribution analysis
- Correlation heatmaps
- Authentication method analysis
- Behavioral pattern analysis
- Boxplots and visual comparisons

### 3. Machine Learning Models
The following models were used:
- Logistic Regression
- Random Forest Classification
- XGBoost Classification

### 4. Model Evaluation
Models were evaluated using:
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix

---

## Key Findings

- Some behavioral variables showed stronger relationships with fraud risk than others.
- Login attempts alone did not strongly differentiate fraudulent transactions from legitimate transactions.
- Anomaly score and transaction velocity showed stronger relationships with fraud risk.
- XGBoost produced the strongest overall predictive performance among the models tested.
- Fraud prediction improved when multiple behavioral variables were analyzed together rather than relying on a single feature.

---

## Ethical Considerations

This project discusses several ethical concerns related to fraud detection systems, including:
- customer privacy
- false positives
- machine learning bias
- explainability and transparency in banking systems

---

## Future Improvements

Potential future improvements include:
- real-time transaction monitoring
- customer segmentation analysis
- deep learning approaches
- larger real-world banking datasets
- adaptive authentication systems

