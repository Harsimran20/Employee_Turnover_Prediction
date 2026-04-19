# Employee_Turnover_Prediction
````md
# Employee Turnover Prediction using Machine Learning

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=for-the-badge&logo=pandas">
  <img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikit-learn">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</p>

---

## Project Overview

Employee turnover is a critical business challenge that affects productivity, hiring costs, and organizational stability.  

This project applies **Machine Learning Classification Models** to predict whether an employee is likely to leave the company based on historical workforce data.

The solution can help HR departments identify at-risk employees early and improve retention strategies.

---

## Business Problem

High employee attrition leads to:

- Increased recruitment and training costs  
- Productivity loss  
- Team disruption  
- Lower employee morale  

Using predictive analytics, organizations can make proactive decisions to reduce turnover.

---

## Objectives

- Predict employee turnover accurately  
- Compare baseline Logistic Regression with regularized models  
- Evaluate model performance using classification metrics  
- Build an interpretable HR analytics solution  

---

## Dataset Information

The dataset contains employee-related features such as:

- Age  
- Salary  
- Experience  
- Department  
- Work Hours  
- Satisfaction Score  
- Performance Metrics  
- Other HR-related indicators  

**Target Variable:**  
- `Employee_Turnover`  
  - `1 = Left Company`  
  - `0 = Stayed`

---

## Technologies Used

| Category | Tools |
|--------|-------|
| Programming Language | Python |
| Data Analysis | Pandas |
| Visualization | Seaborn |
| Machine Learning | Scikit-learn |
| Development Environment | Jupyter Notebook |

---

## Machine Learning Models Implemented

### 1. Logistic Regression
Baseline classification model.

### 2. Lasso Regularization (L1)
Helps with feature selection and reduces overfitting.

### 3. Ridge Regularization (L2)
Improves model generalization by shrinking coefficients.

---

## Project Workflow

```text
Data Collection
      ↓
Data Cleaning
      ↓
Feature Selection
      ↓
Train-Test Split
      ↓
Model Training
      ↓
Prediction
      ↓
Performance Evaluation
````

---

## Evaluation Metrics

The following metrics were used:

* Accuracy Score
* Precision Score
* Classification Report
* Model Comparison

---

## Sample Code

```python
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
```

---

## Project Structure

```bash
employee-turnover-prediction/
│── Employee_Turnover.py
│── employee_turnover.csv
│── README.md
│── requirements.txt
```

---

## Installation & Setup

### Clone Repository

```bash
git clone https://github.com/yourusername/employee-turnover-prediction.git
cd employee-turnover-prediction
```

### Install Dependencies

```bash
pip install pandas seaborn scikit-learn
```

### Run Project

```bash
python Employee_Turnover.py
```

---

## Key Insights

* Logistic Regression provides strong baseline performance
* L1 Regularization removes less important features
* L2 Regularization improves stability and generalization
* Predictive analytics can support employee retention decisions

---

## Future Enhancements

* Hyperparameter tuning using GridSearchCV
* Random Forest / XGBoost implementation
* Feature importance dashboard
* Streamlit Web App deployment
* Power BI HR Dashboard integration

---

## Why This Project Matters

This project demonstrates real-world skills in:

* Data Science
* HR Analytics
* Predictive Modeling
* Model Evaluation
* Business Problem Solving

---
