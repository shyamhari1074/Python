# Pandas - Create DataFrame from 2D List

This repository contains a simple Python solution using **pandas** to create a DataFrame from a 2D list named `student_data`.

## 📝 Problem Statement

Write a solution to create a DataFrame from a 2D list called `student_data`.  
This 2D list contains the IDs and ages of some students.

The DataFrame should:
- Have two columns: `student_id` and `age`
- Preserve the original order of the 2D list

## 📌 Example Input

```python
student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]
```

## ✅ Expected Output

```
   student_id  age
0           1   15
1           2   11
2           3   11
3           4   20
```

## 💡 Solution

```python
import pandas as pd

def createDataframe(student_data):
    df = pd.DataFrame(student_data, columns=["student_id", "age"])
    return df

# Example usage
student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]
print(createDataframe(student_data))
```

### 🔍 Explanation
The `createDataframe` function takes a 2D list as input and uses the `pandas.DataFrame()` constructor to convert it into a DataFrame. The `columns` parameter names the two columns as `student_id` and `age`, maintaining the original order of the data.

## 📦 Requirements

- Python 3.x
- pandas library

You can install the required package using:

```bash
pip install pandas
```

## 📁 Folder Structure

```
pandas/
├── solution.py
└── README.md
```

---

Feel free to contribute or improve the solution!

