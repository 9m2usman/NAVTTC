
# ETL + ETL PERFORMANCE — MIDDLE LEVEL LEARNING PROJECT

## What you are learning

ETL = Extract -> Transform -> Load

You will learn:
1. Extracting data from multiple CSV sources
2. Inspecting schemas and data quality
3. Cleaning missing, duplicate, invalid and inconsistent data
4. Joining multiple datasets
5. Creating derived/business columns
6. Validating the transformed data
7. Loading clean data into a final destination
8. Measuring ETL runtime and memory
9. Finding slow operations
10. Optimizing the same pipeline without changing its output
11. Comparing before vs after performance

Use Python + pandas first. Do NOT jump to Spark yet.

--------------------------------------------------
TASK 1 — COMPLETE ETL PIPELINE
--------------------------------------------------

Goal:
Build a production-style ETL pipeline for an e-commerce company.

Files:
- task1_customers.csv
- task1_products.csv
- task1_orders_raw.csv

Expected flow:

SOURCE FILES
    |
    v
EXTRACT
    |
    v
RAW DATA INSPECTION
    |
    v
TRANSFORM
    |---- remove duplicates
    |---- handle missing values
    |---- standardize city names
    |---- validate quantity
    |---- validate discount
    |---- validate amounts
    |---- join customer data
    |---- join product data
    |---- create calculated columns
    |
    v
DATA QUALITY CHECK
    |
    v
LOAD
    |
    v
clean_orders.csv
clean_customer_summary.csv
clean_product_summary.csv

### Step 1 — Extract

Start by loading all three CSVs with pandas.

Do not clean while reading them.

First store them as:
customers
products
orders

Then print:
- shape
- columns
- dtypes
- missing values
- duplicate count

### Step 2 — Understand relationships

Identify:
orders.customer_id -> customers.customer_id
orders.product_id  -> products.product_id

Write down the relationship before coding the joins.

### Step 3 — Transform

Perform transformations in this order:

A. Remove exact duplicate order rows.

B. Standardize text:
- Lahore / lahore / LHR -> Lahore
- Karachi / KHI -> Karachi
- Islamabad / ISB -> Islamabad

C. Missing values:
- discount_pct -> 0
- payment_method -> "Unknown"
- shipping_city -> customer city when possible, otherwise "Unknown"

D. Validate:
- quantity must be > 0
- discount_pct must be between 0 and 100
- total_amount must be >= 0

Do not silently hide bad records. Create a rejected_records dataset or rejection_reason column.

E. Join:
orders + customers
orders + products

F. Create useful columns:
- gross_amount
- discount_amount
- net_amount
- order_year
- order_month
- is_successful_order

### Step 4 — Data quality checks

Before loading, prove that:

- order_id is unique
- customer_id exists in customer table
- product_id exists in product table
- quantity is valid
- discount is valid
- net_amount is non-negative
- required columns have no unexpected nulls

Print a small ETL report:

rows_extracted
rows_cleaned
rows_rejected
duplicate_rows_removed
missing_values_fixed
final_rows

### Step 5 — Load

Create:

output/
    clean_orders.csv
    rejected_orders.csv
    customer_summary.csv
    product_summary.csv
    etl_report.txt

This is your first complete ETL pipeline.

### Task 1 final goal

You should be able to explain:

"Where did the data come from?
What was wrong with it?
What transformations did I apply?
Why did I apply them?
How did I validate it?
Where did I load it?
How many records were accepted/rejected?"

--------------------------------------------------
TASK 2 — ETL PERFORMANCE ENGINEERING
--------------------------------------------------

Goal:
Take a large transaction pipeline and make it significantly faster
without changing the final result.

Files:
- task2_transactions_1m.csv
- task2_merchants.csv
- task2_accounts.csv
- task2_customers.csv

The main file has 1,000,000 transactions.

### Step 1 — Build the slow/reference version FIRST

Do NOT optimize immediately.

Build a straightforward pandas ETL:

EXTRACT
  |
  v
LOAD 1M transactions
  |
  v
CLEAN
  |
  v
JOIN merchant
  |
  v
JOIN account
  |
  v
JOIN customer
  |
  v
CREATE derived fields
  |
  v
FILTER valid transactions
  |
  v
AGGREGATE
  |
  v
LOAD result

Measure:

- total runtime
- extraction time
- transformation time
- join time
- aggregation time
- output time
- memory usage

Use Python's time.perf_counter().

### Step 2 — Create a performance baseline

Record:

baseline_runtime_seconds
baseline_memory_mb
baseline_output_rows

Do not change the result.

### Step 3 — Find bottlenecks

Investigate these areas:

1. Reading unnecessary columns
2. Wrong dtypes
3. Repeated DataFrame operations
4. Inefficient row-by-row loops
5. Expensive apply()
6. Repeated filtering
7. Inefficient joins
8. Unnecessary copies
9. Recalculating the same expression
10. Loading data that is never used

### Step 4 — Optimize one thing at a time

Optimization order:

Optimization A:
Read only required columns.

Optimization B:
Specify appropriate dtypes while reading.

Optimization C:
Convert repeated string columns to category where appropriate.

Optimization D:
Replace row-by-row loops with vectorized pandas operations.

Optimization E:
Replace unnecessary apply() operations with vectorized operations.

Optimization F:
Filter rows earlier when logically safe.

Optimization G:
Pre-select only required columns before joins.

Optimization H:
Aggregate efficiently.

After EVERY optimization:

1. Run pipeline
2. Measure runtime
3. Compare row count
4. Compare important numeric results
5. Confirm output is equivalent

Never optimize blindly.

### Step 5 — Performance comparison

Create:

performance_results.csv

Columns:

version
runtime_seconds
memory_mb
rows_output
speedup_percent

Example versions:

baseline
read_optimization
dtype_optimization
vectorization
join_optimization
final_optimized

### Step 6 — Final performance report

Your final report should answer:

1. What was the original runtime?
2. What was the final runtime?
3. Which operation was the bottleneck?
4. Which optimization helped most?
5. Did memory usage decrease?
6. Did output remain equivalent?
7. Why did the optimization work?

--------------------------------------------------
THE GENERAL ETL PATTERN TO MEMORIZE
--------------------------------------------------

Every ETL project should mentally follow:

1. EXTRACT
   Read source systems/files.

2. PROFILE
   Understand shape, schema, nulls, duplicates, ranges and relationships.

3. VALIDATE SOURCE
   Identify bad data before transforming it.

4. TRANSFORM
   Clean, standardize, join and derive.

5. VALIDATE TRANSFORMED DATA
   Check business rules and data integrity.

6. LOAD
   Write to the destination.

7. VERIFY OUTPUT
   Confirm row counts, keys, totals and expected structure.

8. MONITOR
   Record runtime, errors, rejected records and data-quality metrics.

For performance work add:

9. BASELINE
10. PROFILE
11. FIND BOTTLENECK
12. OPTIMIZE ONE STEP
13. BENCHMARK AGAIN
14. VERIFY SAME RESULT
15. DOCUMENT THE IMPROVEMENT

--------------------------------------------------
WHAT NOT TO DO
--------------------------------------------------

Do not:
- start with optimization
- use loops for millions of rows
- use apply() for everything
- drop bad rows without recording why
- change the final result just to make it faster
- optimize before measuring
- use Spark simply because the dataset is large
- build a complicated architecture before the pandas pipeline works

--------------------------------------------------
WHEN TO MOVE TO ADVANCED ETL
--------------------------------------------------

After these two tasks, move to:

Python/pandas ETL
    ->
SQL ETL
    ->
PostgreSQL
    ->
incremental ETL
    ->
partitioning
    ->
Parquet
    ->
Airflow
    ->
Spark/PySpark
    ->
cloud ETL

Do not skip the baseline and validation stages.

--------------------------------------------------
SUCCESS CRITERIA
--------------------------------------------------

Task 1:
You can build a complete ETL pipeline from raw data to validated output.

Task 2:
You can prove where an ETL pipeline is slow and demonstrate measurable
performance improvement while preserving the result.

If you can complete both without copying a solution, you have moved
from "I know pandas" toward practical ETL/data-engineering work.
