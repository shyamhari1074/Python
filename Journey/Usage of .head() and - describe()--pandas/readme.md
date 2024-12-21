# DataFrame Summary and Exploration Script 📊

This script demonstrates basic DataFrame operations in Python using the **Pandas** library. It showcases how to inspect a dataset by displaying its first few rows and generating summary statistics.

---

## 🔧 Requirements

Ensure you have the following installed on your system:
- Python 3.x
- Pandas library

Install Pandas using pip if you don't already have it:
```bash
pip install pandas
```

---

## 📄 Code Overview

### Functionality:
1. **Creates a DataFrame** with sample data.
2. **Displays the first few rows** of the DataFrame using `.head()`.
3. **Generates summary statistics** for the DataFrame using `.describe()`.

### Code Snippet:
```python
import pandas as pd

# Sample DataFrame
data = {
    "Feature1": [1, 2, 3, 4, 5],
    "Feature2": [10, 20, 30, 40, 50],
    "Target": [2, 4, 6, 8, 10]
}

df = pd.DataFrame(data)

# Display the first 5 rows
print(df.head())

# Generate summary statistics
print(df.describe())
```

---

## 💡 Key Outputs

1. **`df.head()`**:
   - Displays the first 5 rows of the dataset to inspect its structure.
   
   Example Output:
   ```
      Feature1  Feature2  Target
   0         1        10       2
   1         2        20       4
   2         3        30       6
   3         4        40       8
   4         5        50      10
   ```

2. **`df.describe()`**:
   - Provides summary statistics for all numerical columns in the DataFrame.
   
   Example Output:
   ```
          Feature1   Feature2     Target
   count   5.00000   5.00000   5.000000
   mean    3.00000  30.00000   6.000000
   std     1.58114  15.81139   3.162278
   min     1.00000  10.00000   2.000000
   25%     2.00000  20.00000   4.000000
   50%     3.00000  30.00000   6.000000
   75%     4.00000  40.00000   8.000000
   max     5.00000  50.00000  10.000000
   ```

---

## 🔍 Use Case

This script is useful for:
- Quickly inspecting a dataset during the early stages of data analysis.
- Understanding the distribution and basic statistical properties of your data.

---

## 🖋️ Author

**Shyam Hari**  
[GitHub Profile](https://github.com/shyamhari1074)  

---

## 🌟 Contributions

Feel free to suggest improvements or contribute to this script by creating a pull request!

---

## 🖍️ License

This project is open-source and available under the [MIT License](LICENSE).
