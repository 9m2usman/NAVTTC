import pandas as pd
import os

# STEP 1 — EXTRACT
# Load all three CSV files
# Do not clean anything while reading
customers = pd.read_csv( "E:/navttcPython/3.0.1_ETL_Tasks/task1_customers.csv" )
products = pd.read_csv( "E:/navttcPython/3.0.1_ETL_Tasks/task1_products.csv" )
orders = pd.read_csv( "E:/navttcPython/3.0.1_ETL_Tasks/task1_orders_raw.csv" )

# Initial data information
print("\nCUSTOMERS")
print("Shape:\n",customers.shape,"\n\nColumns:\n",customers.columns,"\n\nData Types:\n",customers.dtypes)
print("\nMissing Values:\n",customers.isnull().sum(),"\n\nDuplicate Count:\n",customers.duplicated().sum())

print("\nPRODUCTS")
print("Shape:\n",products.shape,"\n\nColumns:\n",products.columns,"\n\nData Types:\n",products.dtypes)
print("\nMissing Values:\n",products.isnull().sum(),"\n\nDuplicate Count:\n",products.duplicated().sum())

print("\nORDERS")
print("Shape:\n",orders.shape,"\n\nColumns:\n",orders.columns,"\n\nData Types:\n",orders.dtypes)
print("\nMissing Values:\n",orders.isnull().sum(),"\n\nDuplicate Count:\n",orders.duplicated().sum())

# STEP 2 — UNDERSTAND RELATIONSHIPS
print("\nRELATIONSHIPS")
print("orders.customer_id -> customers.customer_id")
print("orders.product_id  -> products.product_id")

# STEP 3 — TRANSFORM

# A. Remove exact duplicate order rows
rows_before_duplicates = len(orders)
orders = orders.drop_duplicates()
rows_after_duplicates = len(orders)
duplicate_rows_removed = (rows_before_duplicates - rows_after_duplicates)

print("\nDuplicate rows removed:",duplicate_rows_removed)

# B. Standardize text
city_mapping = {
    "Lahore": "Lahore",
    "lahore": "Lahore",
    "LHR": "Lahore",
    "Karachi": "Karachi",
    "KHI": "Karachi",
    "Islamabad": "Islamabad",
    "ISB": "Islamabad"
}

customers["city"] = customers["city"].replace(city_mapping)
orders["shipping_city"] = orders["shipping_city"].replace(city_mapping)

# C. Missing values
missing_values_before = orders.isnull().sum().sum()

# discount_pct -> 0
orders["discount_pct"] = orders["discount_pct"].fillna(0)

# payment_method -> Unknown
orders["payment_method"] = orders["payment_method"].fillna("Unknown")

# shipping_city -> customer city when possible
customer_city = customers[ ["customer_id","city"] ].drop_duplicates( subset=["customer_id"] )

orders = orders.merge( customer_city, on="customer_id", how="left" )

orders["shipping_city"] = orders["shipping_city"].fillna( orders["city"] )
orders["shipping_city"] = orders["shipping_city"].fillna("Unknown")

orders = orders.drop( columns=["city"] )

missing_values_after = orders.isnull().sum().sum()
missing_values_fixed = (missing_values_before - missing_values_after)

print("Missing values fixed:",missing_values_fixed)

# D. VALIDATE
orders["rejection_reason"] = ""

# Quantity must be > 0
invalid_quantity = orders["quantity"] <= 0
orders.loc[ invalid_quantity, "rejection_reason" ] = "Invalid quantity"

# Discount must be between 0 and 100
invalid_discount = ( (orders["discount_pct"] < 0) | (orders["discount_pct"] > 100) )
orders.loc[ invalid_discount, "rejection_reason" ] = (
    orders.loc[ invalid_discount, "rejection_reason" ] +
    "; Invalid discount_pct"
)

# total_amount must be >= 0
invalid_total = orders["total_amount"] < 0
orders.loc[ invalid_total, "rejection_reason" ] = (
    orders.loc[ invalid_total, "rejection_reason" ] +
    "; Invalid total_amount"
)

orders["rejection_reason"] = orders["rejection_reason"].str.strip("; ")

# Create rejected dataset
rejected_orders = orders[ orders["rejection_reason"] != "" ].copy()

# Keep valid orders
orders = orders[ orders["rejection_reason"] == "" ].copy()

rows_rejected = len(rejected_orders)

print("Rejected rows:",rows_rejected)

# E. JOIN ORDERS + CUSTOMERS
orders = orders.merge( customers, on="customer_id", how="left" )

# F. JOIN ORDERS + PRODUCTS
orders = orders.merge( products, on="product_id", how="left" )

# G. CREATE USEFUL COLUMNS

# Gross amount
orders["gross_amount"] = (
    orders["quantity"] * orders["unit_price"]
)

# Discount amount
orders["discount_amount"] = (
    orders["gross_amount"] *
    orders["discount_pct"] / 100
)

# Net amount
orders["net_amount"] = (
    orders["gross_amount"] -
    orders["discount_amount"]
)

# Convert order date to datetime
orders["order_date"] = pd.to_datetime(
    orders["order_date"],
    errors="coerce"
)

# Order year
orders["order_year"] = orders["order_date"].dt.year

# Order month
orders["order_month"] = orders["order_date"].dt.month

# Order month name
orders["order_month_name"] = orders["order_date"].dt.month_name()

# Order day
orders["order_day"] = orders["order_date"].dt.day

# Order day name
orders["order_day_name"] = orders["order_date"].dt.day_name()

# Order quarter
orders["order_quarter"] = orders["order_date"].dt.quarter

# Successful order
orders["is_successful_order"] = (
    (orders["payment_method"] != "Unknown") &
    (orders["net_amount"] >= 0)
)

# Order size
orders["order_size"] = "Small"

orders.loc[
    orders["quantity"] >= 5,
    "order_size"
] = "Medium"

orders.loc[
    orders["quantity"] >= 10,
    "order_size"
] = "Large"

# STEP 4 — DATA QUALITY CHECKS

# 1. order_id must be unique
order_id_unique = orders["order_id"].is_unique
print("\nOrder ID is unique:",order_id_unique)

# 2. customer_id exists in customer table
customer_ids = set(customers["customer_id"])

missing_customer_ids = orders[
    ~orders["customer_id"].isin(customer_ids)
]

print("Missing customer IDs:",len(missing_customer_ids))

# 3. product_id exists in product table
product_ids = set(products["product_id"])

missing_product_ids = orders[
    ~orders["product_id"].isin(product_ids)
]

print("Missing product IDs:",len(missing_product_ids))

# 4. quantity is valid
invalid_quantity_after = orders[
    orders["quantity"] <= 0
]

print("Invalid quantity records:",len(invalid_quantity_after))

# 5. discount is valid
invalid_discount_after = orders[
    (orders["discount_pct"] < 0) |
    (orders["discount_pct"] > 100)
]

print("Invalid discount records:",len(invalid_discount_after))

# 6. net_amount is non-negative
invalid_net_amount = orders[
    orders["net_amount"] < 0
]

print("Negative net amount records:",len(invalid_net_amount))

# 7. Required columns should not have unexpected nulls
required_columns = [
    "order_id",
    "customer_id",
    "product_id",
    "quantity",
    "discount_pct",
    "total_amount",
    "gross_amount",
    "discount_amount",
    "net_amount"
]

print("\nRequired column missing values:")

for column in required_columns:

    missing_count = orders[column].isnull().sum()

    print(column,":",missing_count)

# Overall quality result
quality_check_passed = (
    order_id_unique and
    len(missing_customer_ids) == 0 and
    len(missing_product_ids) == 0 and
    len(invalid_quantity_after) == 0 and
    len(invalid_discount_after) == 0 and
    len(invalid_net_amount) == 0
)

print("\nOverall data quality passed:",quality_check_passed)

# CUSTOMER SUMMARY
customer_summary = orders.groupby(
    "customer_id"
).agg(
    total_orders=("order_id","count"),
    total_quantity=("quantity","sum"),
    total_spent=("net_amount","sum"),
    average_order_value=("net_amount","mean")
).reset_index()

# PRODUCT SUMMARY
product_summary = orders.groupby(
    "product_id"
).agg(
    total_orders=("order_id","count"),
    total_quantity=("quantity","sum"),
    total_revenue=("net_amount","sum"),
    average_order_value=("net_amount","mean")
).reset_index()

# CITY SUMMARY
city_summary = orders.groupby(
    "city"
).agg(
    total_orders=("order_id","count"),
    total_quantity=("quantity","sum"),
    total_revenue=("net_amount","sum"),
    average_order_value=("net_amount","mean")
).reset_index()

# MONTHLY SUMMARY
monthly_summary = orders.groupby(
    ["order_year","order_month","order_month_name"]
).agg(
    total_orders=("order_id","count"),
    total_quantity=("quantity","sum"),
    total_revenue=("net_amount","sum"),
    average_order_value=("net_amount","mean")
).reset_index()

# ORDER SIZE SUMMARY
order_size_summary = orders.groupby(
    "order_size"
).agg(
    total_orders=("order_id","count"),
    total_quantity=("quantity","sum"),
    total_revenue=("net_amount","sum")
).reset_index()

# STEP 5 — LOAD

# Create output directory
os.makedirs(
    "3.0.1_ETL_Tasks/output",
    exist_ok=True
)

# Save clean orders
orders.to_csv(
    "3.0.1_ETL_Tasks/output/clean_orders.csv",
    index=False
)

# Save rejected orders
rejected_orders.to_csv(
    "3.0.1_ETL_Tasks/output/rejected_orders.csv",
    index=False
)

# Save customer summary
customer_summary.to_csv(
    "3.0.1_ETL_Tasks/output/customer_summary.csv",
    index=False
)

# Save product summary
product_summary.to_csv(
    "3.0.1_ETL_Tasks/output/product_summary.csv",
    index=False
)

# Save city summary
city_summary.to_csv(
    "3.0.1_ETL_Tasks/output/city_summary.csv",
    index=False
)

# Save monthly summary
monthly_summary.to_csv(
    "3.0.1_ETL_Tasks/output/monthly_summary.csv",
    index=False
)

# Save order size summary
order_size_summary.to_csv(
    "3.0.1_ETL_Tasks/output/order_size_summary.csv",
    index=False
)

# ETL REPORT
rows_extracted = len(
    pd.read_csv(
        "3.0.1_ETL_Tasks/task1_orders_raw.csv"
    )
)

rows_cleaned = len(orders)
final_rows = len(orders)

etl_report = f"""
ETL REPORT

SOURCE DATA
Rows extracted: {rows_extracted}

TRANSFORMATION
Duplicate rows removed: {duplicate_rows_removed}
Missing values fixed: {missing_values_fixed}

VALIDATION
Rows cleaned/accepted: {rows_cleaned}
Rows rejected: {rows_rejected}

FINAL DATA
Final rows: {final_rows}

DATA QUALITY
Order ID unique: {order_id_unique}
Missing customer IDs: {len(missing_customer_ids)}
Missing product IDs: {len(missing_product_ids)}
Invalid quantity records: {len(invalid_quantity_after)}
Invalid discount records: {len(invalid_discount_after)}
Negative net amount records: {len(invalid_net_amount)}

Overall quality passed: {quality_check_passed}

OUTPUT FILES
output/clean_orders.csv
output/rejected_orders.csv
output/customer_summary.csv
output/product_summary.csv
output/city_summary.csv
output/monthly_summary.csv
output/order_size_summary.csv
output/etl_report.txt
"""

print("\n")
print(etl_report)

# Save ETL report
with open(
    "3.0.1_ETL_Tasks/output/etl_report.txt",
    "w"
) as file:

    file.write(etl_report)

print("ETL pipeline completed successfully.")