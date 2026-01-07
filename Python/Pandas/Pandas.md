# 🐼 Pandas Cheat Sheet (Beginner → Intermediate)

Pandas is the most popular Python library for data analysis, cleaning, transformation, and file operations.

---

## 📦 Installation & Import

```python
pip install pandas
````

```python
import pandas as pd
```

---

## 🧱 Core Data Structures

### DataFrame (2D - Table)

```python
df = pd.DataFrame({
    "name": ["A", "B"],
    "age": [25, 30]
})
```

### Series (1D - Column)

```python
s = pd.Series([25, 30])
```

---

## 📥 Load Data

```python
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")
df = pd.read_json("data.json")
```

---

## 🔍 Basic Exploration

```python
df.head()       # first 5 rows
df.tail()       # last 5 rows
df.info()       # schema + nulls + types
df.describe()   # statistics (numerical data)
df.shape        # (rows, columns)
```

---

## 🔍 Selecting Data

```python
df['age']              # select one column
df[['name','age']]     # select multiple columns
df.iloc[0]             # row by index
df.loc[0,'name']       # row + column by label
```

---

## 🧹 Data Cleaning

```python
df.dropna()            # remove rows with null values
df.fillna(0)           # replace null values
df.drop_duplicates()   # remove duplicates

df['price'] = df['price'].astype(float)   # change data type
```

---

## 🎯 Filtering & Conditional Selection

```python
df[df['age'] > 25]
df[(df['age'] > 25) & (df['city'] == "Delhi")]
```

---

## ➕ Add, Update, Delete

```python
df['country'] = "India"      # add column
df.drop(columns=['age'])     # delete column
df.rename(columns={'name':'full_name'}, inplace=True)
```

---

## 🔗 Joins & Combining

```python
pd.merge(df1, df2, on='id')     # SQL join
pd.concat([df1, df2])           # stack vertically
```

---

## 📊 Grouping & Aggregations

```python
df.groupby('city')['salary'].mean()
df.groupby('dept').agg({'salary':['sum','mean']})
```

---

## 🔄 Sorting & Index

```python
df.sort_values(by='salary', ascending=False)
df.set_index('id', inplace=True)
```

---

## 🗂️ Export Files

```python
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
```

---

## 🧠 Useful Notes

| Concept               | Meaning                        |
| --------------------- | ------------------------------ |
| `NaN`                 | Missing/Null value             |
| `inplace=True`        | Modify original DataFrame      |
| Vectorized Operations | Faster than looping            |
| DataFrame = Table     | Easy transition from SQL/Excel |

---

## 💡 Real World Use Cases

| Field            | Uses                          |
| ---------------- | ----------------------------- |
| Backend APIs     | Format DB → JSON output       |
| Data Engineering | ETL: Clean and transform data |
| Analytics        | Generate reports              |
| Machine Learning | Feature engineering           |

