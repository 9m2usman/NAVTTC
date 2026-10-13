import pandas as pd
import os

# STEP 1 — EXTRACT
# Load all three CSV files
# Do not clean anything while reading
customers = pd.read_csv( "E:/navttcPython/3.0.1_ETL_Tasks/task1_customers.csv" )
products = pd.read_csv( "E:/navttcPython/3.0.1_ETL_Tasks/task1_products.csv" )
orders = pd.read_csv( "E:/navttcPython/3.0.1_ETL_Tasks/task1_orders_raw.csv" )

# Initial data information
print("\n================ CUSTOMERS ================")
print("Shape:\n",customers.shape,"\n\nColumns:\n",customers.columns,"\n\nData Types:\n",customers.dtypes)
print("\nMissing Values:\n",customers.isnull().sum(),"\n\nDuplicate Count:\n",customers.duplicated().sum())

print("\n================ PRODUCTS ================")
print("Shape:\n",products.shape,"\n\nColumns:\n",products.columns,"\n\nData Types:\n",products.dtypes)
print("\nMissing Values:\n",products.isnull().sum(),"\n\nDuplicate Count:\n",products.duplicated().sum())

print("\n================ ORDERS ================")
print("Shape:\n",orders.shape,"\n\nColumns:\n",orders.columns,"\n\nData Types:\n",orders.dtypes)
print("\nMissing Values:\n",orders.isnull().sum(),"\n\nDuplicate Count:\n",orders.duplicated().sum())

# STEP 2 — UNDERSTAND RELATIONSHIPS
print("\n================ RELATIONSHIPS ================")
print("orders.customer_id -> customers.customer_id")
print("orders.product_id  -> products.product_id")

# STEP 3 — TRANSFORM
# A. Remove exact duplicate order rows
rows_before_duplicates = len(orders)
orders = orders.drop_duplicates()
rows_after_duplicates = len(orders)
duplicate_rows_removed = (rows_before_duplicates - rows_after_duplicates)
print("\n================ DUPLICATES ================")
print("Duplicate rows removed:", duplicate_rows_removed)

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

# Standardize customer city
customers["city"] = customers["city"].replace(city_mapping)

# Standardize shipping city
orders["shipping_city"] = orders["shipping_city"].replace(city_mapping)

# C. Missing values
missing_values_before = orders.isnull().sum().sum()

# discount_pct -> 0
orders["discount_pct"] = orders["discount_pct"].fillna(0)

# payment_method -> Unknown
orders["payment_method"] = orders["payment_method"].fillna("Unknown")

# shipping_city -> customer city when possible
# Get customer city using customer_id
customer_city = customers[ ["customer_id", "city"] ].drop_duplicates( subset=["customer_id"] )

# Temporarily join customer city
orders = orders.merge( customer_city, on="customer_id", how="left" )

# Use customer city when shipping city is missing
orders["shipping_city"] = orders["shipping_city"].fillna( orders["city"] )

# If customer city is also missing
orders["shipping_city"] = orders["shipping_city"].fillna("Unknown")

# Remove temporary city column
orders = orders.drop( columns=["city"] )
missing_values_after = orders.isnull().sum().sum()
missing_values_fixed = (missing_values_before - missing_values_after)
print("\n================ MISSING VALUES ================")
print("Missing values fixed:", missing_values_fixed)

# D. VALIDATE
# Create rejection reason column
orders["rejection_reason"] = ""

# Quantity must be > 0
invalid_quantity = orders["quantity"] <= 0
orders.loc[ invalid_quantity, "rejection_reason" ] = "Invalid quantity"

# Discount must be between 0 and 100
invalid_discount = ( (orders["discount_pct"] < 0) | (orders["discount_pct"] > 100) )
orders.loc[ invalid_discount, "rejection_reason" ] = ( orders.loc[ invalid_discount, "rejection_reason" ] + "; Invalid discount_pct" )

# total_amount must be >= 0
invalid_total = orders["total_amount"] < 0
orders.loc[ invalid_total, "rejection_reason" ] = ( orders.loc[ invalid_total, "rejection_reason" ] + "; Invalid total_amount" )

# Remove unnecessary semicolon/space
orders["rejection_reason"] = ( orders["rejection_reason"].str.strip("; ") )

# Create rejected dataset
rejected_orders = orders[ orders["rejection_reason"] != "" ].copy()

# Keep valid orders
orders = orders[ orders["rejection_reason"] == "" ].copy()
rows_rejected = len(rejected_orders)
print("\n================ VALIDATION ================")
print("Rejected rows:", rows_rejected)

# E. JOIN ORDERS + CUSTOMERS
orders = orders.merge( customers, on="customer_id", how="left" )

# E. JOIN ORDERS + PRODUCTS
orders = orders.merge( products, on="product_id", how="left" )

# F. CREATE USEFUL COLUMNS
# Gross amount
orders["gross_amount"] = ( orders["quantity"] * orders["unit_price"] )

# Discount amount
orders["discount_amount"] = ( orders["gross_amount"] * orders["discount_pct"] / 100 )

# Net amount
orders["net_amount"] = ( orders["gross_amount"] - orders["discount_amount"] )

# Convert order date to datetime
orders["order_date"] = pd.to_datetime( orders["order_date"], errors="coerce" )

# Order year
orders["order_year"] = ( orders["order_date"].dt.year )


# Order month
orders["order_month"] = ( orders["order_date"].dt.month )

# Successful order
orders["is_successful_order"] = ( (orders["payment_method"] != "Unknown") & (orders["net_amount"] >= 0) )

# STEP 4 — DATA QUALITY CHECKS
print("\n================ DATA QUALITY CHECKS ================")


# 1. order_id must be unique
order_id_unique = ( orders["order_id"].is_unique )
print( "order_id is unique:", order_id_unique )

# 2. customer_id exists in customer table
customer_ids = set( customers["customer_id"] )
missing_customer_ids = orders[ ~orders["customer_id"].isin(customer_ids) ] # ~this symbol mean true -> false and false -> true
# as orders["customers_id"].isin(customer_ids) that matches ids in orders table with customer_ids that is taken from customer table and this return tru and false
print( "Missing customer IDs:", len(missing_customer_ids) )

# 3. product_id exists in product table
product_ids = set( products["product_id"] )
missing_product_ids = orders[ ~orders["product_id"].isin(product_ids) ]
print( "Missing product IDs:", len(missing_product_ids) )

# 4. quantity is valid
invalid_quantity_after = orders[ orders["quantity"] <= 0 ]
print( "Invalid quantity records:", len(invalid_quantity_after) )

# 5. discount is valid
invalid_discount_after = orders[ (orders["discount_pct"] < 0) | (orders["discount_pct"] > 100) ]
print( "Invalid discount records:", len(invalid_discount_after) )

# 6. net_amount is non-negative
invalid_net_amount = orders[ orders["net_amount"] < 0 ]
print( "Negative net amount records:", len(invalid_net_amount) )

# 7. Required columns should not have unexpected nulls
required_columns = [ "order_id","customer_id","product_id","quantity","discount_pct","total_amount","gross_amount","discount_amount","net_amount" ]
print("\nRequired column missing values:")
for column in required_columns:
    missing_count = orders[column].isnull().sum()
    print( column, ":", missing_count )

# Overall quality result
quality_check_passed = ( order_id_unique and len(missing_customer_ids) == 0 and len(missing_product_ids) == 0 and len(invalid_quantity_after) == 0 and len(invalid_discount_after) == 0 and len(invalid_net_amount) == 0 )
print( "\nOverall data quality passed:", quality_check_passed )

# CREATE CUSTOMER SUMMARY
customer_summary = orders.groupby( "customer_id" ).agg(
    total_orders=("order_id", "count"),
    total_spent=("net_amount", "sum"),
    average_order_value=("net_amount", "mean")
).reset_index()

# CREATE PRODUCT SUMMARY
product_summary = orders.groupby( "product_id" ).agg(
    total_orders=("order_id", "count"),
    total_quantity=("quantity", "sum"),
    total_revenue=("net_amount", "sum"),
    average_order_value=("net_amount", "mean")
).reset_index()


# STEP 5 — LOAD
# Create output directory
os.makedirs( "3.0.1_ETL_Tasks/output", exist_ok=True )

# Save clean orders
orders.to_csv( "3.0.1_ETL_Tasks/output/clean_orders.csv", index=False )

# Save rejected orders
rejected_orders.to_csv( "3.0.1_ETL_Tasks/output/rejected_orders.csv", index=False )

# Save customer summary
customer_summary.to_csv( "3.0.1_ETL_Tasks/output/customer_summary.csv", index=False )

# Save product summary
product_summary.to_csv( "3.0.1_ETL_Tasks/output/product_summary.csv", index=False )

# ETL REPORT
rows_extracted = len(pd.read_csv("3.0.1_ETL_Tasks/task1_orders_raw.csv"))
rows_cleaned = len(orders)
final_rows = len(orders)

etl_report = f"""
================ ETL REPORT ================

SOURCE DATA
--------------------------------------------
Rows extracted: {rows_extracted}

TRANSFORMATION
--------------------------------------------
Duplicate rows removed: {duplicate_rows_removed}
Missing values fixed: {missing_values_fixed}

VALIDATION
--------------------------------------------
Rows cleaned/accepted: {rows_cleaned}
Rows rejected: {rows_rejected}

FINAL DATA
--------------------------------------------
Final rows: {final_rows}

DATA QUALITY
--------------------------------------------
Order ID unique: {order_id_unique}
Missing customer IDs: {len(missing_customer_ids)}
Missing product IDs: {len(missing_product_ids)}
Invalid quantity records: {len(invalid_quantity_after)}
Invalid discount records: {len(invalid_discount_after)}
Negative net amount records: {len(invalid_net_amount)}

Overall quality passed: {quality_check_passed}

OUTPUT FILES
--------------------------------------------
output/clean_orders.csv
output/rejected_orders.csv
output/customer_summary.csv
output/product_summary.csv
output/etl_report.txt
"""
print("\n")
print(etl_report)

# Save ETL report
with open( "3.0.1_ETL_Tasks/output/etl_report.txt", "w" ) as file:
    file.write(etl_report)

print("ETL pipeline completed successfully.")