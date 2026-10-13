# FILE 2 — csv_visualization.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Task 23 — Create and Read students.csv
df = pd.read_csv("students.csv")

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()
print(df.describe())


# Task 24 — CSV Filtering

df = pd.read_csv("students.csv")

print(df[df["marks"] > 80])

print(df[df["city"] == "Lahore"])

print(df[df["age"] > 20])

print(
    df[
        (df["city"] == "Lahore") &
        (df["marks"] > 80)
    ]
)


# Task 25 — CSV Statistics

df = pd.read_csv("students.csv")

print("Mean:", df["marks"].mean())
print("Median:", df["marks"].median())
print("Mode:", df["marks"].mode().tolist())
print("Highest:", df["marks"].max())
print("Lowest:", df["marks"].min())
print("Total:", df["marks"].sum())
print("Count:", df["marks"].count())


# Task 26 — CSV Cleaning

df = pd.read_csv("employees.csv")

print(df)

print(df.isnull().sum())

df["age"] = df["age"].fillna(
    df["age"].mean()
)

df["salary"] = df["salary"].fillna(
    df["salary"].median()
)

df["city"] = df["city"].fillna(
    "Unknown"
)

df = df.drop_duplicates()

df.to_csv(
    "employees_cleaned.csv",
    index=False
)

print(df)


# Task 27 — Pandas Bar Chart

data = {
    "department": ["IT", "HR", "Sales"],
    "revenue": [500000, 300000, 700000]
}

df = pd.DataFrame(data)

df.plot(
    x="department",
    y="revenue",
    kind="bar"
)

plt.title("Department Revenue")
plt.xlabel("Department")
plt.ylabel("Revenue")

plt.show()


# Task 28 — Line Chart

data = {
    "month": [
        "January",
        "February",
        "March",
        "April",
        "May"
    ],
    "sales": [
        100000,
        120000,
        90000,
        150000,
        180000
    ]
}

df = pd.DataFrame(data)

df.plot(
    x="month",
    y="sales",
    kind="line",
    marker="o"
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()


# Task 29 — Pie Chart

data = {
    "department": [
        "IT",
        "HR",
        "Sales",
        "Marketing"
    ],
    "employees": [
        30,
        20,
        40,
        10
    ]
}

df = pd.DataFrame(data)

plt.pie(
    df["employees"],
    labels=df["department"],
    autopct="%1.1f%%"
)

plt.title("Employees by Department")

plt.show()


# Task 30 — Histogram

marks = [
    45, 50, 55, 60,
    65, 70, 72, 75,
    80, 85, 90, 95
]

plt.hist(
    marks,
    bins=5
)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Students")

plt.show()


# Task 31 — Seaborn Bar Plot

data = {
    "department": ["IT", "HR", "Sales"],
    "salary": [60000, 50000, 80000]
}

df = pd.DataFrame(data)

sns.barplot(
    data=df,
    x="department",
    y="salary"
)

plt.title("Department Salary")

plt.show()


# Task 32 — Seaborn Count Plot

data = {
    "department": [
        "IT", "IT", "HR",
        "Sales", "IT", "HR",
        "Sales", "Sales"
    ]
}

df = pd.DataFrame(data)

sns.countplot(
    data=df,
    x="department"
)

plt.title("Employees by Department")

plt.show()


# Task 33 — Seaborn Scatter Plot

data = {
    "age": [21, 23, 25, 27, 30],
    "salary": [40000, 45000, 55000, 65000, 80000]
}

df = pd.DataFrame(data)

sns.scatterplot(
    data=df,
    x="age",
    y="salary"
)

plt.title("Age vs Salary")

plt.show()


# Task 34 — Seaborn Histogram

data = {
    "salary": [
        40000,
        45000,
        50000,
        55000,
        60000,
        65000,
        70000,
        75000,
        80000
    ]
}

df = pd.DataFrame(data)

sns.histplot(
    data=df,
    x="salary",
    bins=5,
    kde=True
)

plt.title("Salary Distribution")

plt.show()


# Task 35 — Seaborn Box Plot

data = {
    "salary": [
        40000,
        45000,
        50000,
        55000,
        60000,
        65000,
        70000,
        300000
    ]
}

df = pd.DataFrame(data)

sns.boxplot(
    data=df,
    y="salary"
)

plt.title("Salary Box Plot")

plt.show()


# Task 36 — Seaborn Heatmap

data = {
    "Math": [80, 90, 70, 85],
    "English": [70, 85, 60, 80],
    "Computer": [90, 95, 75, 90],
    "Physics": [75, 88, 65, 82]
}

df = pd.DataFrame(data)

correlation = df.corr()

print(correlation)

sns.heatmap(
    correlation,
    annot=True
)

plt.title("Subject Correlation")

plt.show()


# Task 37 — Sales CSV Analysis

sales_data = """employee,department,city,sales
Ali,IT,Lahore,50000
Usman,IT,Islamabad,70000
Ahmed,HR,Lahore,40000
Sara,HR,Karachi,60000
Hina,Sales,Lahore,90000
Hamza,Sales,Islamabad,80000
"""

with open("sales.csv", "w") as file:
    file.write(sales_data)

df = pd.read_csv("sales.csv")

print("Total Sales:")
print(df["sales"].sum())

print("Average Sales:")
print(df["sales"].mean())

department_sales = df.groupby(
    "department"
)["sales"].sum()

print("Sales by Department:")
print(department_sales)

city_sales = df.groupby(
    "city"
)["sales"].sum()

print("Sales by City:")
print(city_sales)

department_chart = (
    df.groupby("department", as_index=False)["sales"]
    .sum()
)

sns.barplot(
    data=department_chart,
    x="department",
    y="sales"
)

plt.title("Total Sales by Department")

plt.show()


# Task 38 — Complete Employee Analytics System

company_data = """id,name,age,department,city,salary,experience,performance
1,Ali,22,IT,Lahore,50000,1,78
2,Usman,25,IT,Islamabad,70000,3,91
3,Ahmed,28,HR,Lahore,60000,5,85
4,Sara,24,HR,Karachi,,2,88
5,Hina,30,Sales,Lahore,80000,6,95
6,Hamza,,Sales,Islamabad,75000,4,72
7,Ayesha,27,IT,Lahore,65000,4,89
8,Bilal,29,Sales,Karachi,90000,7,96
9,Zara,23,HR,Lahore,55000,2,
10,Ali,22,IT,Lahore,50000,1,78
11,Usman,25,IT,Islamabad,70000,3,91
12,Noor,26,HR,Karachi,58000,3,82
13,Hassan,31,Sales,Lahore,85000,8,94
14,Maria,24,IT,Lahore,,2,76
15,Kamran,27,HR,Islamabad,62000,4,87
"""

with open("company_employees.csv", "w") as file:
    file.write(company_data)


# Read CSV

df = pd.read_csv(
    "company_employees.csv"
)

print(df)


# First 5 rows

print(df.head())


# Shape

print(df.shape)


# Columns

print(df.columns)


# Data Types

print(df.dtypes)


# Information

df.info()


# Missing Values

print(df.isnull().sum())


# Duplicates

print(df[df.duplicated()])


# Fill Missing Age

df["age"] = df["age"].fillna(
    df["age"].mean()
)


# Fill Missing Salary

df["salary"] = df["salary"].fillna(
    df["salary"].median()
)


# Fill Missing Performance

df["performance"] = df["performance"].fillna(
    df["performance"].mean()
)


# Remove Duplicates

df = df.drop_duplicates()


# Clean City

df["city"] = df["city"].str.strip()
df["city"] = df["city"].str.title()


# Performance Status

df["performance_status"] = df["performance"].apply(
    lambda x:
        "Good" if x >= 80
        else "Needs Improvement"
)


# Salary Level

def salary_level(salary):

    if salary >= 80000:
        return "High"

    elif salary >= 60000:
        return "Medium"

    else:
        return "Low"


df["salary_level"] = df["salary"].apply(
    salary_level
)


# Mean Salary

print(df["salary"].mean())


# Median Salary

print(df["salary"].median())


# Mode City

print(df["city"].mode())


# Highest Salary

print(df["salary"].max())


# Lowest Salary

print(df["salary"].min())


# Salary > 60000

print(
    df[df["salary"] > 60000]
)


# Performance > 85

print(
    df[df["performance"] > 85]
)


# IT Employees

print(
    df[df["department"] == "IT"]
)


# Lahore Employees

print(
    df[df["city"] == "Lahore"]
)


# IT + Performance > 85

print(
    df[
        (df["department"] == "IT") &
        (df["performance"] > 85)
    ]
)


# Salary Descending

print(
    df.sort_values(
        "salary",
        ascending=False
    )
)


# Department Average Salary

department_average_salary = df.groupby(
    "department"
)["salary"].mean()

print(department_average_salary)


# Department Employee Count

department_employee_count = df.groupby(
    "department"
)["id"].count()

print(department_employee_count)


# Department Maximum Salary

department_max_salary = df.groupby(
    "department"
)["salary"].max()

print(department_max_salary)


# Department Average Performance

department_average_performance = df.groupby(
    "department"
)["performance"].mean()

print(department_average_performance)


# City Employee Count

city_employee_count = df["city"].value_counts()

print(city_employee_count)


# Complete Department Report

department_report = df.groupby(
    "department"
).agg(
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max"),
    average_performance=("performance", "mean"),
    employee_count=("id", "count")
)

print(department_report)


# Save Cleaned CSV

df.to_csv(
    "company_employees_cleaned.csv",
    index=False
)


# Chart 1 — Employees by Department

sns.countplot(
    data=df,
    x="department"
)

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Employee Count")

plt.show()


# Chart 2 — Average Salary

average_salary_chart = (
    df.groupby("department", as_index=False)["salary"]
    .mean()
)

sns.barplot(
    data=average_salary_chart,
    x="department",
    y="salary"
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.show()


# Chart 3 — Salary Distribution

sns.histplot(
    data=df,
    x="salary",
    bins=6,
    kde=True
)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Employee Count")

plt.show()


# Chart 4 — Age vs Salary

sns.scatterplot(
    data=df,
    x="age",
    y="salary",
    hue="department"
)

plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")

plt.show()


# Chart 5 — Performance Distribution

sns.histplot(
    data=df,
    x="performance",
    bins=6,
    kde=True
)

plt.title("Performance Distribution")
plt.xlabel("Performance")
plt.ylabel("Employee Count")

plt.show()