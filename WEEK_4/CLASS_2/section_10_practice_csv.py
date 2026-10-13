import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Load dataset
df = pd.read_csv("navttc/2.0PthonLib&ELD/Books_Data_Clean.csv")


# 2. Display settings
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_rows", 100)


# 3. Basic dataset information
print("\n================ FIRST 10 ROWS ================\n")
print(df.head(10))

print("\n================ LAST 10 ROWS ================\n")
print(df.tail(10))

print("\n================ RANDOM 10 ROWS ================\n")
print(df.sample(10))

print("\n================ SHAPE ================\n")
print(df.shape)

print("\n================ COLUMN NAMES ================\n")
print(df.columns.tolist())

print("\n================ DATA TYPES ================\n")
print(df.dtypes)

print("\n================ INFO ================\n")
df.info()


# 4. Missing value analysis
print("\n================ MISSING VALUES ================\n")
print(df.isnull().sum())

print("\n================ MISSING PERCENTAGE ================\n")
missing_percentage = (df.isnull().sum() / len(df)) * 100
print(missing_percentage)

print("\n================ ROWS WITH MISSING VALUES ================\n")
print(df[df.isnull().any(axis=1)])


# 5. Duplicate analysis
print("\n================ DUPLICATE ROW COUNT ================\n")
print(df.duplicated().sum())

print("\n================ DUPLICATE BOOK NAMES ================\n")
print(df["Book Name"].duplicated().sum())

print("\n================ DUPLICATE BOOK NAME ROWS ================\n")

duplicate_books = df[
    df["Book Name"].duplicated(keep=False)
].sort_values("Book Name")

print(
    duplicate_books[
        [
            "Book Name",
            "Author",
            "Publishing Year",
            "Publisher "
        ]
    ]
)


# 6. Unique values
print("\n================ UNIQUE COUNTS ================\n")
print(df.nunique())

print("\n================ GENRE VALUES ================\n")
print(df["genre"].unique())

print("\n================ LANGUAGE VALUES ================\n")
print(df["language_code"].unique())

print("\n================ AUTHOR RATING VALUES ================\n")
print(df["Author_Rating"].unique())

print("\n================ PUBLISHER VALUES ================\n")
print(df["Publisher "].unique())


# 7. Value counts
print("\n================ GENRE COUNTS ================\n")
print(df["genre"].value_counts())

print("\n================ LANGUAGE COUNTS ================\n")
print(df["language_code"].value_counts(dropna=False))

print("\n================ AUTHOR RATING COUNTS ================\n")
print(df["Author_Rating"].value_counts())

print("\n================ PUBLISHER COUNTS ================\n")
print(df["Publisher "].value_counts())


# 8. Statistical EDA
print("\n================ NUMERIC STATISTICS ================\n")
print(df.describe())

print("\n================ CATEGORICAL STATISTICS ================\n")
print(df.describe(include="object"))

print("\n================ COMPLETE STATISTICS ================\n")
print(df.describe(include="all"))


# 9. Identify numeric and categorical columns
numeric_columns = df.select_dtypes(
    include="number"
).columns

categorical_columns = df.select_dtypes(
    include="object"
).columns

print("\n================ NUMERIC COLUMNS ================\n")
print(numeric_columns.tolist())

print("\n================ CATEGORICAL COLUMNS ================\n")
print(categorical_columns.tolist())


# 10. Check suspicious publishing years
print("\n================ MINIMUM PUBLISHING YEAR ================\n")
print(df["Publishing Year"].min())

print("\n================ MAXIMUM PUBLISHING YEAR ================\n")
print(df["Publishing Year"].max())

print("\n================ NEGATIVE PUBLISHING YEARS ================\n")
print(
    df[df["Publishing Year"] < 0][
        [
            "Publishing Year",
            "Book Name",
            "Author"
        ]
    ]
)

# 11. Check invalid numeric values
print("\n================ INVALID RATINGS ================\n")
print(
    df[
        (df["Book_average_rating"] < 0) |
        (df["Book_average_rating"] > 5)
    ]
)

print("\n================ INVALID SALE PRICES ================\n")
print(
    df[df["sale price"] <= 0]
)

print("\n================ INVALID UNITS SOLD ================\n")
print(
    df[df["units sold"] <= 0]
)

print("\n================ INVALID GROSS SALES ================\n")
print(
    df[df["gross sales"] < 0]
)

print("\n================ INVALID PUBLISHER REVENUE ================\n")
print(
    df[df["publisher revenue"] < 0]
)


# 12. Clean column names
df.columns = df.columns.str.strip()

print("\n================ CLEANED COLUMN NAMES ================\n")
print(df.columns.tolist())


# 13. Clean text columns
text_columns = [
    "Book Name",
    "Author",
    "language_code",
    "Author_Rating",
    "genre",
    "Publisher"
]

for column in text_columns:
    df[column]  = df[column].str.strip()

# 14. Handle missing values
# Book Name is text, so use a text placeholder
df["Book Name"] = df["Book Name"].fillna("Unknown")

# language_code is categorical
df["language_code"] = df["language_code"].fillna("Unknown")

# Publishing Year has only one missing value.
# We use median here rather than mean because median is less affected by unusual historical years.
median_year = df["Publishing Year"].median()

df["Publishing Year"] = df["Publishing Year"].fillna(
    median_year
)


# 15. Verify cleaning
print("\n================ MISSING VALUES AFTER CLEANING ================\n")
print(df.isnull().sum())

print("\n================ DUPLICATES AFTER CLEANING ================\n")
print(df.duplicated().sum())


# 16. Filtering
print("\n================ RATING > 4 ================\n")

high_rating_books = df[
    df["Book_average_rating"] > 4
]

print(high_rating_books.head(20))


print("\n================ UNITS SOLD > 10,000 ================\n")

high_sales_books = df[
    df["units sold"] > 10000
]

print(high_sales_books.head(20))


print("\n================ SALE PRICE > 5 ================\n")

expensive_books = df[
    df["sale price"] > 5
]

print(expensive_books.head(20))


# 17. Multiple conditions
print("\n================ RATING > 4 AND UNITS > 10,000 ================\n")

filtered_books = df[
    (df["Book_average_rating"] > 4) &
    (df["units sold"] > 10000)
]

print(filtered_books.head(20))


print("\n================ PRICE > 5 AND SALES > 1,000 ================\n")

filtered_sales = df[
    (df["sale price"] > 5) &
    (df["gross sales"] > 1000)
]

print(filtered_sales.head(20))


# 18. Sorting
print("\n================ HIGHEST GROSS SALES ================\n")

print(
    df.sort_values(
        "gross sales",
        ascending=False
    ).head(10)
)


print("\n================ MOST UNITS SOLD ================\n")

print(
    df.sort_values(
        "units sold",
        ascending=False
    ).head(10)
)


print("\n================ HIGHEST RATINGS ================\n")

print(
    df.sort_values(
        "Book_average_rating",
        ascending=False
    ).head(10)
)


# 19. Groupby analysis
print("\n================ AVERAGE RATING BY GENRE ================\n")

print(
    df.groupby("genre")[
        "Book_average_rating"
    ].mean()
)


print("\n================ AVERAGE SALES BY GENRE ================\n")

print(
    df.groupby("genre")[
        "gross sales"
    ].mean()
)


print("\n================ TOTAL UNITS SOLD BY GENRE ================\n")

print(
    df.groupby("genre")[
        "units sold"
    ].sum()
)


print("\n================ AVERAGE PRICE BY PUBLISHER ================\n")

print(
    df.groupby("Publisher")[
        "sale price"
    ].mean()
)


# 20. Multiple aggregations
print("\n================ GENRE AGGREGATION ================\n")

genre_analysis = df.groupby("genre").agg({
    "gross sales": ["mean", "sum"],
    "units sold": ["mean", "sum"],
    "sale price": "mean",
    "Book_average_rating": "mean",
    "Book_ratings_count": "mean"
})

print(genre_analysis)


# 21. Correlation
print("\n================ CORRELATION MATRIX ================\n")

correlation = df.corr(
    numeric_only=True
)

print(correlation)


print("\n================ PRICE VS UNITS CORRELATION ================\n")

print(
    df["sale price"].corr(
        df["units sold"]
    )
)


print("\n================ RATING VS SALES CORRELATION ================\n")

print(
    df["Book_average_rating"].corr(
        df["gross sales"]
    )
)


print("\n================ RATINGS COUNT VS SALES CORRELATION ================\n")

print(
    df["Book_ratings_count"].corr(
        df["gross sales"]
    )
)


# 22. Visualization

# Histogram
plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="sale price",
    bins=7
)

plt.title("Distribution of Book Sale Prices")
plt.xlabel("Sale Price")
plt.ylabel("Number of Books")

plt.show()


# Rating histogram
plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="Book_average_rating",
    bins=20
)

plt.title("Distribution of Book Ratings")
plt.xlabel("Average Rating")
plt.ylabel("Number of Books")

plt.show()


# Genre count
plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="genre"
)

plt.title("Number of Books by Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Books")

plt.xticks(rotation=30)

plt.show()


# Sales by genre
plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="genre",
    y="gross sales"
)

plt.title("Average Gross Sales by Genre")
plt.xlabel("Genre")
plt.ylabel("Gross Sales")

plt.xticks(rotation=30)

plt.show()


# Price vs units
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="sale price",
    y="units sold"
)

plt.title("Sale Price vs Units Sold")
plt.xlabel("Sale Price")
plt.ylabel("Units Sold")

plt.show()


# Rating vs sales
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Book_average_rating",
    y="gross sales"
)

plt.title("Book Rating vs Gross Sales")
plt.xlabel("Average Rating")
plt.ylabel("Gross Sales")

plt.show()


# Sales boxplot
plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="gross sales"
)

plt.title("Gross Sales Distribution")
plt.ylabel("Gross Sales")

plt.show()


# Units sold boxplot
plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    y="units sold"
)

plt.title("Units Sold Distribution")
plt.ylabel("Units Sold")

plt.show()


# 23. Correlation heatmap
plt.figure(figsize=(12, 8))

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.show()


# 24. Top 10 books by sales
top_sales = df.sort_values(
    "gross sales",
    ascending=False
).head(10)

print("\n================ TOP 10 BOOKS BY GROSS SALES ================\n")

print(
    top_sales[
        [
            "Book Name",
            "Author",
            "gross sales",
            "units sold",
            "sale price"
        ]
    ]
)


# 25. Top 10 books by units sold
top_units = df.sort_values(
    "units sold",
    ascending=False
).head(10)

print("\n================ TOP 10 BOOKS BY UNITS SOLD ================\n")

print(
    top_units[
        [
            "Book Name",
            "Author",
            "units sold",
            "gross sales",
            "sale price"
        ]
    ]
)


# 26. Top authors by number of books
print("\n================ TOP AUTHORS ================\n")

print(
    df["Author"].value_counts().head(10)
)


# 27. Top publishers by number of books
print("\n================ TOP PUBLISHERS ================\n")

print(
    df["Publisher"].value_counts().head(10)
)


# 28. Save cleaned dataset
df.to_csv(
    "Books_Data_Cleaned_Final.csv",
    index=False
)

print(
    "\nCleaned dataset saved as "
    "Books_Data_Cleaned_Final.csv"
)