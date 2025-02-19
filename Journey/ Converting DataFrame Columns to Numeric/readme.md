# Converting DataFrame Columns to Numeric in Pandas

### Understanding `pd.to_numeric(errors='coerce')`

When working with datasets, columns may contain mixed data types (numbers and strings). `pd.to_numeric(errors='coerce')` helps convert them into numeric types while handling errors gracefully.

## Code Example

```python
import pandas as pd

# Create a sample DataFrame with mixed data types
data = {
    'A': ['1', '2', '3', 'four', '5'],  # Contains a non-numeric string "four"
    'B': ['10.5', '20.3', 'xyz', '40.2', '50.1']  # Contains a non-numeric string "xyz"
}

df = pd.DataFrame(data)

print("Before applying pd.to_numeric:")
print(df)

# Convert columns to numeric, forcing errors to NaN
df = df.apply(pd.to_numeric, errors='coerce')

print("\nAfter applying pd.to_numeric(errors='coerce'):")
print(df)
```

## Output

### Before Applying:
```
     A     B
0    1  10.5
1    2  20.3
2    3   xyz
3  four  40.2
4    5  50.1
```

### After Applying `pd.to_numeric(errors='coerce')`:
```
     A     B
0  1.0  10.5
1  2.0  20.3
2  3.0   NaN
3  NaN  40.2
4  5.0  50.1
```

## Explanation:
- The `pd.to_numeric` function converts column values into numbers.
- `"four"` in column `A` and `"xyz"` in column `B` couldn't be converted, so they became `NaN`.
- All valid numeric values were converted to floats.

## When to Use `errors='coerce'`?
- When you expect some non-numeric values in your dataset.
- When you want to replace invalid values with `NaN` instead of raising errors.
- Useful for preprocessing before machine learning or analysis.

This method ensures your dataset remains clean and ready for numerical computations!
