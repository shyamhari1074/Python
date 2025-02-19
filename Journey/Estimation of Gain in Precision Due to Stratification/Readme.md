# Estimation of Gain in Precision Due to Stratification

## Overview
This document explains how to estimate the **gain in precision** when using stratification in train-test splitting for a classification task. The experiment is performed using logistic regression on a dataset related to **credit default prediction**.

## Libraries Used
- `pandas`: For data manipulation
- `scikit-learn`: For machine learning and evaluation metrics

## Steps Involved

### 1. Load and Preprocess Data
- Load the dataset from a CSV file.
- Define **features (X)** and **target (y)**.
- Convert all columns to numeric, handling non-numeric values.
- Fill missing values with the **mean** of the respective columns.

### 2. Train a Baseline Model (Without Stratification)
- Split the data into **training (80%)** and **testing (20%)** sets.
- Train a **logistic regression model**.
- Evaluate **precision score**.

### 3. Train a Stratified Model
- Perform a stratified train-test split, ensuring that **class distribution** is preserved.
- Train another logistic regression model.
- Evaluate **precision score**.

### 4. Calculate Gain in Precision
- Compute the difference between stratified and baseline precision scores.

## Python Code
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
df = pd.read_csv("train.csv")
X = df.drop(columns=["Credit Default", "Id"])
y = df["Credit Default"]

# Convert categorical columns to one-hot encoding if necessary
categorical_cols = X.select_dtypes(include=['object']).columns
if len(categorical_cols) > 0:
    X = pd.get_dummies(X, columns=categorical_cols)

# Handle missing values (basic approach)
X = X.fillna(X.mean())
scaler = StandardScaler()
X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

# Split data without stratification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train baseline model
model = LogisticRegression()
model.fit(X_train, y_train)

# Get predictions and calculate precision
baseline_preds = model.predict(X_test)
baseline_precision = precision_score(y_test, baseline_preds, average="binary")
X_train_strat, X_test_strat, y_train_strat, y_test_strat = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Train model on stratified data
model_strat = LogisticRegression()
model_strat.fit(X_train_strat, y_train_strat)

# Get predictions and calculate stratified precision
stratified_preds = model_strat.predict(X_test_strat)
stratified_precision = precision_score(y_test_strat, stratified_preds, average="binary")

# Calculate gain in precision
gain_in_precision = stratified_precision - baseline_precision

# Output results
print(f"Baseline Precision: {baseline_precision:.4f}")
print(f"Stratified Precision: {stratified_precision:.4f}")
print(f"Gain in Precision: {gain_in_precision:.4f}")
```

## Expected Output
The script will print:
- **Baseline Precision** (without stratification)
- **Stratified Precision** (with stratification)
- **Gain in Precision** (difference between the two)

## Conclusion
Using **stratification** ensures that each class is proportionally represented in training and testing sets, often leading to an improvement in **precision**. This method is particularly useful when dealing with **imbalanced datasets**.

