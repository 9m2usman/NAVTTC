import pandas as pd
import requests
import sqlite3

# STEP 1 — EXTRACT
products_url = "https://dummyjson.com/products?limit=0"
users_url = "https://dummyjson.com/users?limit=0"
carts_url = "https://dummyjson.com/carts?limit=0"

products_response = requests.get(products_url,timeout=30)
print("Products API Status:",products_response.status_code)
products_response.raise_for_status()
products_data = products_response.json()
products = pd.DataFrame(products_data["products"])

users_response = requests.get(users_url,timeout=30)
print("Users API Status:",users_response.status_code)
users_response.raise_for_status()
users_data = users_response.json()
users = pd.DataFrame(users_data["users"])

carts_response = requests.get(carts_url,timeout=30)
print("Carts API Status:",carts_response.status_code)
carts_response.raise_for_status()
carts_data = carts_response.json()
carts = pd.DataFrame(carts_data["carts"])

print()
print("EXTRACTED DATA")
print("Products:",products.shape)
print("Users:",users.shape)
print("Carts:",carts.shape)

print()
print(products.head())
print()
print(users.head())
print()
print(carts.head())

# STEP 2 — TRANSFORM
products["price"] = pd.to_numeric(products["price"],errors="coerce")
products["category"] = products["category"].str.strip().str.title()
products["title"] = products["title"].str.strip()
products = products.drop_duplicates(subset=["id"])
products = products[["id","title","price","category"]]

users["firstName"] = users["firstName"].str.strip()
users["lastName"] = users["lastName"].str.strip()
users["email"] = users["email"].str.strip().str.lower()
users["phone"] = users["phone"].astype(str).str.strip()
users["city"] = users["address"].apply(lambda x: x["city"])
users = users.drop_duplicates(subset=["id"])
users = users[["id","firstName","lastName","email","city","phone"]]

cart_rows = []

for cart in carts.to_dict("records"):
    for item in cart["products"]:
        cart_rows.append({
            "cart_id":cart["id"],
            "user_id":cart["userId"],
            "product_id":item["id"],
            "quantity":item["quantity"],
            "unit_price":item["price"]
        })

cart_items = pd.DataFrame(cart_rows)
cart_items["quantity"] = pd.to_numeric(cart_items["quantity"],errors="coerce")
cart_items["unit_price"] = pd.to_numeric(cart_items["unit_price"],errors="coerce")
cart_items = cart_items.dropna(subset=["cart_id","user_id","product_id","quantity","unit_price"])
cart_items["cart_id"] = cart_items["cart_id"].astype(int)
cart_items["user_id"] = cart_items["user_id"].astype(int)
cart_items["product_id"] = cart_items["product_id"].astype(int)
cart_items["quantity"] = cart_items["quantity"].astype(int)
cart_items["sales_amount"] = cart_items["quantity"] * cart_items["unit_price"]

print()
print("TRANSFORMED DATA")
print()
print("Products:")
print(products.head())
print()
print("Users:")
print(users.head())
print()
print("Cart Items:")
print(cart_items.head())

# STEP 3 — CREATE OLTP DATABASE
connection = sqlite3.connect("ecommerce_oltp.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS order_items")
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS customers")

cursor.execute("""
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        city TEXT,
        phone TEXT
    )
""")

cursor.execute("""
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        price REAL,
        category TEXT
    )
""")

cursor.execute("""
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    )
""")

cursor.execute("""
    CREATE TABLE order_items (
        order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        unit_price REAL,
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )
""")

# STEP 4 — LOAD DATA INTO OLTP
for row in users.itertuples(index=False):
    cursor.execute("""
        INSERT INTO customers (customer_id,first_name,last_name,email,city,phone)
        VALUES (?, ?, ?, ?, ?, ?)
    """,(int(row.id),row.firstName,row.lastName,row.email,row.city,row.phone))

for row in products.itertuples(index=False):
    cursor.execute("""
        INSERT INTO products (product_id,product_name,price,category)
        VALUES (?, ?, ?, ?)
    """,(int(row.id),row.title,float(row.price),row.category))

orders = carts[["id","userId"]].copy()
orders.columns = ["order_id","customer_id"]

for row in orders.itertuples(index=False):
    cursor.execute("""
        INSERT INTO orders (order_id,customer_id)
        VALUES (?, ?)
    """,(int(row.order_id),int(row.customer_id)))

for row in cart_items.itertuples(index=False):
    cursor.execute("""
        INSERT INTO order_items (order_id,product_id,quantity,unit_price)
        VALUES (?, ?, ?, ?)
    """,(int(row.cart_id),int(row.product_id),int(row.quantity),float(row.unit_price)))

connection.commit()

print()
print("OLTP DATABASE CREATED")
print("Customers:",pd.read_sql("SELECT * FROM customers",connection).shape)
print("Products:",pd.read_sql("SELECT * FROM products",connection).shape)
print("Orders:",pd.read_sql("SELECT * FROM orders",connection).shape)
print("Order Items:",pd.read_sql("SELECT * FROM order_items",connection).shape)

# STEP 5 — EXTRACT FROM OLTP
sales_data = pd.read_sql("""
    SELECT
        o.order_id,c.customer_id,c.first_name,c.last_name,c.city,
        p.product_id,p.product_name,p.category,
        oi.quantity,oi.unit_price
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
""",connection)

print()
print("DATA EXTRACTED FROM OLTP")
print("Rows:",sales_data.shape[0])
print("Columns:",sales_data.shape[1])
print()
print(sales_data.head())

# STEP 6 — TRANSFORM FOR OLAP
sales_data["quantity"] = pd.to_numeric(sales_data["quantity"])
sales_data["unit_price"] = pd.to_numeric(sales_data["unit_price"])
sales_data["sales_amount"] = sales_data["quantity"] * sales_data["unit_price"]

# DummyJSON does not provide transaction dates for carts
orders["order_date"] = pd.Timestamp("2026-01-01") + pd.to_timedelta(orders["order_id"],unit="D")

sales_data = sales_data.merge(orders[["order_id","order_date"]],on="order_id",how="left")
sales_data["year"] = sales_data["order_date"].dt.year
sales_data["month"] = sales_data["order_date"].dt.month
sales_data["month_name"] = sales_data["order_date"].dt.month_name()

print()
print("OLAP TRANSFORMED DATA")
print(sales_data.head())

# STEP 7 — CREATE OLAP TABLES
dim_customer = sales_data[["customer_id","first_name","last_name","city"]].drop_duplicates()
dim_product = sales_data[["product_id","product_name","category"]].drop_duplicates()
dim_date = sales_data[["order_date","year","month","month_name"]].drop_duplicates()

fact_sales = sales_data[["order_id","customer_id","product_id","order_date","quantity","unit_price","sales_amount"]].copy()

print()
print("OLAP TABLES")
print("Dim Customer:",dim_customer.shape)
print("Dim Product:",dim_product.shape)
print("Dim Date:",dim_date.shape)
print("Fact Sales:",fact_sales.shape)

# STEP 8 — LOAD DATA INTO OLAP WAREHOUSE
olap_connection = sqlite3.connect("ecommerce_olap.db")

dim_customer.to_sql("dim_customer",olap_connection,if_exists="replace",index=False)
dim_product.to_sql("dim_product",olap_connection,if_exists="replace",index=False)
dim_date.to_sql("dim_date",olap_connection,if_exists="replace",index=False)
fact_sales.to_sql("fact_sales",olap_connection,if_exists="replace",index=False)

print()
print("DATA LOADED INTO OLAP WAREHOUSE")
print("Dim Customer:",pd.read_sql("SELECT * FROM dim_customer",olap_connection).shape)
print("Dim Product:",pd.read_sql("SELECT * FROM dim_product",olap_connection).shape)
print("Dim Date:",pd.read_sql("SELECT * FROM dim_date",olap_connection).shape)
print("Fact Sales:",pd.read_sql("SELECT * FROM fact_sales",olap_connection).shape)

# STEP 9 — VERIFY OLAP WAREHOUSE
warehouse_customers = pd.read_sql("SELECT * FROM dim_customer LIMIT 5",olap_connection)
warehouse_products = pd.read_sql("SELECT * FROM dim_product LIMIT 5",olap_connection)
warehouse_dates = pd.read_sql("SELECT * FROM dim_date LIMIT 5",olap_connection)
warehouse_sales = pd.read_sql("SELECT * FROM fact_sales LIMIT 5",olap_connection)

print()
print("DATA READ BACK FROM OLAP WAREHOUSE")
print()
print("Dim Customer:")
print(warehouse_customers)
print()
print("Dim Product:")
print(warehouse_products)
print()
print("Dim Date:")
print(warehouse_dates)
print()
print("Fact Sales:")
print(warehouse_sales)

# STEP 10 — ANALYTICAL QUERIES
total_revenue = pd.read_sql("""
    SELECT SUM(sales_amount) AS total_revenue
    FROM fact_sales
""",olap_connection)

print()
print("TOTAL REVENUE")
print(total_revenue)

total_orders = pd.read_sql("""
    SELECT COUNT(DISTINCT order_id) AS total_orders
    FROM fact_sales
""",olap_connection)

print()
print("TOTAL ORDERS")
print(total_orders)

total_customers = pd.read_sql("""
    SELECT COUNT(DISTINCT customer_id) AS total_customers
    FROM fact_sales
""",olap_connection)

print()
print("TOTAL CUSTOMERS")
print(total_customers)

sales_by_category = pd.read_sql("""
    SELECT
        p.category,
        SUM(f.quantity) AS units_sold,
        SUM(f.sales_amount) AS total_sales
    FROM fact_sales f
    JOIN dim_product p ON f.product_id = p.product_id
    GROUP BY p.category
    ORDER BY total_sales DESC
""",olap_connection)

print()
print("SALES BY CATEGORY")
print(sales_by_category)

sales_by_customer = pd.read_sql("""
    SELECT
        c.customer_id,c.first_name,c.last_name,c.city,
        SUM(f.sales_amount) AS total_sales
    FROM fact_sales f
    JOIN dim_customer c ON f.customer_id = c.customer_id
    GROUP BY c.customer_id,c.first_name,c.last_name,c.city
    ORDER BY total_sales DESC
""",olap_connection)

print()
print("SALES BY CUSTOMER")
print(sales_by_customer)

sales_by_product = pd.read_sql("""
    SELECT
        p.product_id,p.product_name,p.category,
        SUM(f.quantity) AS units_sold,
        SUM(f.sales_amount) AS total_sales
    FROM fact_sales f
    JOIN dim_product p ON f.product_id = p.product_id
    GROUP BY p.product_id,p.product_name,p.category
    ORDER BY total_sales DESC
""",olap_connection)

print()
print("SALES BY PRODUCT")
print(sales_by_product)

monthly_sales = pd.read_sql("""
    SELECT
        d.year,d.month,d.month_name,
        SUM(f.sales_amount) AS total_sales
    FROM fact_sales f
    JOIN dim_date d ON f.order_date = d.order_date
    GROUP BY d.year,d.month,d.month_name
    ORDER BY d.year,d.month
""",olap_connection)

print()
print("MONTHLY SALES")
print(monthly_sales)

# STEP 11 — BUSINESS KPIs
kpis = pd.read_sql("""
    SELECT
        COUNT(DISTINCT order_id) AS total_orders,
        COUNT(DISTINCT customer_id) AS total_customers,
        SUM(quantity) AS total_units_sold,
        SUM(sales_amount) AS total_revenue,
        AVG(sales_amount) AS average_order_value
    FROM fact_sales
""",olap_connection)

print()
print("BUSINESS KPIs")
print(kpis)

# STEP 12 — CLOSE DATABASE CONNECTIONS
connection.close()
olap_connection.close()

print()
print("ETL PIPELINE COMPLETED")
print("OLTP database: ecommerce_oltp.db")
print("OLAP database: ecommerce_olap.db")