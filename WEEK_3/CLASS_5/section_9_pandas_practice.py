# FILE 1 — pandas_basics.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1 — Create DataFrame

data = {
    "name": ["Ali", "Usman", "Ahmed", "Sara", "Hina"],
    "age": [20, 22, 21, 20, 23],
    "marks": [85, 72, 91, 67, 78],
    "city": ["Lahore", "Islamabad", "Lahore", "Karachi", "Lahore"]
}

df = pd.DataFrame(data)

print(df)


# Task 2 — Series and DataFrame

names = pd.Series(["Ali", "Usman", "Ahmed", "Sara"])
marks = pd.Series([85, 72, 91, 67])

print(names)
print(marks)

data = {
    "name": ["Ali", "Usman", "Ahmed", "Sara"],
    "marks": [85, 72, 91, 67]
}

df = pd.DataFrame(data)

print(df)


# Task 3 — Select Columns

data = {
    "product": ["Laptop", "Phone", "Tablet", "Monitor"],
    "category": ["Computer", "Mobile", "Mobile", "Computer"],
    "price": [80000, 50000, 35000, 30000],
    "stock": [10, 20, 15, 8]
}

df = pd.DataFrame(data)

print(df["product"])
print(df["price"])
print(df[["product", "price"]])
print(df[["product", "category", "stock"]])


# Task 4 — Filter Rows

data = {
    "name": ["Ali", "Usman", "Ahmed", "Sara", "Hina"],
    "marks": [85, 72, 91, 45, 78],
    "city": ["Lahore", "Islamabad", "Lahore", "Karachi", "Lahore"]
}

df = pd.DataFrame(data)

print(df[df["marks"] > 80])
print(df[df["marks"] < 50])
print(df[df["city"] == "Lahore"])


# Task 5 — Multiple Conditions

data = {
    "name": ["Ali", "Usman", "Ahmed", "Sara", "Hina"],
    "department": ["IT", "IT", "HR", "Sales", "HR"],
    "salary": [50000, 75000, 60000, 80000, 55000],
    "experience": [2, 4, 5, 6, 2]
}

df = pd.DataFrame(data)

result = df[(df["salary"] > 60000) & (df["experience"] > 3)]

print(result)

result = df[ (df["department"] == "IT") | (df["department"] == "HR") ]

print(result)


# Task 6 — Sorting

data = {
    "product": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"],
    "price": [80000, 50000, 35000, 30000, 5000],
    "stock": [10, 20, 15, 8, 50]
}

df = pd.DataFrame(data)

print(df.sort_values("price"))
print(df.sort_values("price", ascending=False))
print(df.sort_values("stock", ascending=False))


# Task 7 — Unique Values

data = {
    "customer": ["Ali", "Usman", "Ahmed", "Sara", "Hina"],
    "city": ["Lahore", "Lahore", "Karachi", "Islamabad", "Lahore"],
    "product": ["Laptop", "Phone", "Laptop", "Tablet", "Phone"]
}

df = pd.DataFrame(data)

print(df["city"].unique())
print(df["product"].unique())
print(df["city"].nunique())


# Task 8 — value_counts()

data = {
    "employee": [
        "Ali", "Usman", "Ahmed",
        "Sara", "Hina", "Hamza", "Zara"
    ],
    "department": [
        "IT", "IT", "HR",
        "Sales", "IT", "HR", "Sales"
    ]
}

df = pd.DataFrame(data)

print(df["department"].value_counts())


# Task 9 — apply()

data = {
    "name": ["Ali", "Usman", "Ahmed", "Sara", "Hina"],
    "marks": [92, 75, 64, 48, 85]
}

df = pd.DataFrame(data)


def calculate_grade(marks):

    if marks >= 90:
        return "A+"

    elif marks >= 80:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 50:
        return "D"

    else:
        return "F"


df["grade"] = df["marks"].apply(calculate_grade)

print(df)


# Task 10 — Mean, Median, Maximum, Minimum

data = {
    "employee": ["Ali", "Usman", "Ahmed", "Sara", "Hina"],
    "salary": [50000, 60000, 55000, 70000, 65000]
}

df = pd.DataFrame(data)

print(df["salary"].mean())
print(df["salary"].median())
print(df["salary"].max())
print(df["salary"].min())


# Task 11 — Mode

data = {
    "customer": ["Ali", "Usman", "Ahmed", "Sara", "Hina", "Hamza"],
    "city": [
        "Lahore",
        "Lahore",
        "Karachi",
        "Lahore",
        "Islamabad",
        "Lahore"
    ]
}

df = pd.DataFrame(data)

print(df["city"].mode())


# Task 12 — Mean vs Median

data = {
    "salary": [40000, 45000, 50000, 55000, 500000]
}

df = pd.DataFrame(data)

print(df["salary"].mean())
print(df["salary"].median())


# Task 13 — Missing Data

data = {
    "name": ["Ali", "Usman", "Ahmed", "Sara", "Hina"],
    "age": [20, None, 22, 21, 23],
    "salary": [50000, 60000, None, 55000, 70000],
    "city": ["Lahore", "Islamabad", "Lahore", None, "Lahore"]
}

df = pd.DataFrame(data)

print(df.isnull())
print(df.isnull().sum())


# Task 14 — Fill Missing Salary

data = {
    "name": ["Ali", "Usman", "Ahmed", "Sara", "Hina"],
    "salary": [50000, 60000, None, 55000, 70000]
}

df = pd.DataFrame(data)

median_salary = df["salary"].median()

df["salary"] = df["salary"].fillna(median_salary)

print(df)


# Task 15 — Fill Missing Text

data = {
    "name": ["Ali", "Usman", "Ahmed", "Sara"],
    "city": ["Lahore", None, "Karachi", None]
}

df = pd.DataFrame(data)

df["city"] = df["city"].fillna("Unknown")

print(df)


# Task 16 — dropna()

data = {
    "name": ["Ali", "Usman", "Ahmed", "Sara"],
    "age": [20, None, 22, 21],
    "marks": [85, 72, None, 67]
}

df = pd.DataFrame(data)

df = df.dropna()

print(df)


# Task 17 — Duplicate Cleaning

data = {
    "id": [1, 2, 3, 4],
    "name": ["Ali", "Usman", "Ali", "Ahmed"],
    "salary": [50000, 60000, 50000, 55000]
}

df = pd.DataFrame(data)

print(df[df.duplicated()])

df = df.drop_duplicates()

print(df)


# Task 18 — Clean Text

data = {
    "name": ["Ali", "Usman", "Ahmed", "Sara"],
    "city": [" Lahore ", "lahore", "LAHORE", " Karachi "]
}

df = pd.DataFrame(data)

df["city"] = df["city"].str.strip()
df["city"] = df["city"].str.title()

print(df)


# Task 19 — GroupBy Average Salary

data = {
    "name": ["Ali", "Usman", "Ahmed", "Sara", "Hina"],
    "department": ["IT", "IT", "HR", "HR", "Sales"],
    "salary": [50000, 70000, 45000, 55000, 80000]
}

df = pd.DataFrame(data)

result = df.groupby("department")["salary"].mean()

print(result)


# Task 20 — Department Statistics

data = {
    "name": ["Ali", "Usman", "Ahmed", "Sara", "Hina", "Hamza"],
    "department": ["IT", "IT", "HR", "HR", "Sales", "Sales"],
    "salary": [50000, 70000, 45000, 55000, 80000, 75000]
}

df = pd.DataFrame(data)

result = df.groupby("department")["salary"].agg(
    ["mean", "max", "min", "count"]
)

print(result)


# Task 21 — Merge

employees = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Ali", "Usman", "Ahmed"],
    "department": ["IT", "HR", "Sales"]
})

salaries = pd.DataFrame({
    "id": [1, 2, 3],
    "salary": [50000, 60000, 70000]
})

result = pd.merge(
    employees,
    salaries,
    on="id"
)

print(result)


# Task 22 — Concat

january = pd.DataFrame({
    "product": ["Laptop", "Phone"],
    "sales": [100000, 50000]
})

february = pd.DataFrame({
    "product": ["Laptop", "Phone"],
    "sales": [120000, 60000]
})

result = pd.concat(
    [january, february],
    ignore_index=True
)

print(result)