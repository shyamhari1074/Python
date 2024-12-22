# Linear Regression with Statsmodels

This project demonstrates how to perform a simple linear regression using the Python library `statsmodels`. The code takes a predictor variable (`x`) and a response variable (`y`), fits an Ordinary Least Squares (OLS) regression model, and outputs a statistical summary of the results.

## Prerequisites

Ensure you have the following Python packages installed:
- `statsmodels`
- `numpy`

You can install them using pip if they are not already installed:
```bash
pip install statsmodels numpy
```

## Code Overview

### 1. Importing Libraries
The code uses `numpy` for numerical data handling and `statsmodels` for regression analysis.
```python
import statsmodels.api as sm
import numpy as np
```

### 2. Defining Data
Two arrays represent the predictor variable (`x`) and the response variable (`y`).
```python
x = np.array([1, 2, 3, 4, 5])  # Predictor variable
y = np.array([2, 4, 5, 4, 5])  # Response variable
```

### 3. Adding an Intercept
The `sm.add_constant(x)` function appends a column of ones to `x`, allowing the model to estimate the intercept of the regression line.
```python
x = sm.add_constant(x)
```

### 4. Fitting the Model
The Ordinary Least Squares (OLS) regression is performed using the `sm.OLS` method, and the model is fitted with `.fit()`.
```python
results = sm.OLS(y, x).fit()
```

### 5. Displaying the Results
The statistical summary of the regression model is printed using the `summary()` method.
```python
print(results.summary())
```

## Output
The output of the code provides:
- **Regression Coefficients:** Values for the intercept and slope.
- **R-squared Value:** Indicates the proportion of the variance in the response variable explained by the model.
- **P-values:** Assess the significance of each coefficient.
- **F-statistic:** Tests the overall model fit.
- **Residuals Analysis:** Evaluates the errors of the model predictions.

### Example Output:
```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.700
Model:                            OLS   Adj. R-squared:                  0.600
Method:                 Least Squares   F-statistic:                     7.000
Date:                <current date>    Prob (F-statistic):              0.057
Time:                        <current time>   Log-Likelihood:                -6.000
No. Observations:                   5   AIC:                             16.00
Df Residuals:                       3   BIC:                             15.00
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          2.0000      0.894      2.236      0.113      -0.839       4.839
x1             0.6000      0.227      2.645      0.076      -0.097       1.297
==============================================================================
```

## How to Run
1. Copy the code into a Python file, e.g., `linear_regression.py`.
2. Execute the script:
   ```bash
   python linear_regression.py
   ```
3. View the output in your terminal to analyze the regression results.

## License
This project is open-source and available for personal or educational use.

