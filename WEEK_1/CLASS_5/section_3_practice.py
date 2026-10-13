# 4. IF / ELIF / ELSE — 5 High-Level Tasks
# Task 1 — Advanced Electricity Bill Calculator

# Take electricity units from the user.

# Calculate the bill according to:

# Units	Rate
# 0–100	Rs. 10/unit
# 101–200	Rs. 15/unit
# 201–300	Rs. 20/unit
# 301–500	Rs. 25/unit
# Above 500	Rs. 30/unit

# Additional rules:

# If the bill exceeds Rs. 10,000 → add 5% surcharge.
# If the bill exceeds Rs. 20,000 → add 10% surcharge instead.
# If units are negative → display "Invalid units".

# Finally display:

# Units
# Base Bill
# Surcharge
# Final Bill
# Task 2 — University Admission Eligibility

# Take these values from the user:

# Matric percentage
# FSc percentage
# Entry test percentage
# Interview score

# Rules:

# Reject immediately if:
# Matric < 50%
# FSc < 50%
# Entry test < 40%

# Otherwise:

# Calculate:
# Final Score =
# FSc × 0.40
# + Entry Test × 0.40
# + Interview × 0.20

# Admission category:

# 90+       → Full Scholarship
# 80–89     → Merit Admission
# 70–79     → Normal Admission
# 60–69     → Waiting List
# Below 60  → Rejected

# Also handle invalid percentages such as:

# -10
# 105
# Task 3 — ATM Transaction System

# Ask the user for:

# Current balance
# Transaction type
# Amount

# Transaction types:

# 1 → Withdraw
# 2 → Deposit
# 3 → Check Balance
# Withdrawal rules:
# Amount must be positive.
# Amount must be a multiple of 500.
# If amount > balance → insufficient balance.
# If balance after withdrawal would be below Rs. 500 → reject transaction.
# Deposit rules:
# Amount must be positive.
# Amount above Rs. 100,000 → reject.

# Display the appropriate message and final balance.

# Task 4 — Employee Salary & Tax Calculator

# Take:

# Employee name
# Basic salary
# Years of experience
# Performance rating

# Bonus:

# Experience >= 5 years → 20%
# Experience 3–4 years  → 10%
# Experience 1–2 years  → 5%
# Otherwise             → 0%

# Performance bonus:

# Rating >= 90 → 15%
# Rating >= 75 → 10%
# Rating >= 60 → 5%
# Otherwise    → 0%

# Tax:

# Salary <= 50,000       → 0%
# 50,001–100,000         → 5%
# 100,001–200,000        → 10%
# Above 200,000          → 15%

# Calculate:

# Basic Salary
# Experience Bonus
# Performance Bonus
# Gross Salary
# Tax
# Final Salary
# Task 5 — Smart Shipping Calculator

# Take:

# Order amount
# Customer city
# Customer type
# Delivery speed

# Customer types:

# regular
# premium
# business

# Delivery:

# standard
# express

# Rules:

# Regular customer
# Order >= 5000 → Free standard delivery
# Otherwise → Rs. 300
# Premium customer
# Always free standard delivery
# Business customer
# Order >= 3000 → Free standard delivery
# Otherwise → Rs. 150
# Express delivery

# Add:

# Rs. 500

# unless the customer is premium, in which case:

# Rs. 250

# Special city rule:

# Lahore → no extra charge
# Islamabad → Rs. 100
# Karachi → Rs. 200
# Other cities → Rs. 300

# Finally display:

# Order Amount
# Customer Type
# Delivery Type
# City
# Delivery Charges
# Final Amount

# task 1
electricity_units = int(input("Enter electricity units: "))
if electricity_units < 0:
    print("Invalid units")
else:
    # Calculate the bill based on units
    if 0 <= electricity_units <= 100:
        bill = electricity_units * 10
    elif 101 <= electricity_units <= 200:
        bill = 100 * 10 + (electricity_units - 100) * 15
    elif 201 <= electricity_units <= 300:
        bill = 100 * 10 + 100 * 15 + (electricity_units - 200) * 20
    elif 301 <= electricity_units <= 500:
        bill = 100 * 10 + 100 * 15 + 100 * 20 + (electricity_units - 300) * 25
    else:
        bill = 100 * 10 + 100 * 15 + 100 * 20 + 200 * 25 + (electricity_units - 500) * 30  

    # Apply surcharge if necessary
    if bill > 20000:
        surcharge = bill * 0.10
    elif bill > 10000:
        surcharge = bill * 0.05
    else:
        surcharge = 0

    final_bill = bill + surcharge

    print(f"Units: {electricity_units}")
    print(f"Base Bill: Rs. {bill}")
    print(f"Surcharge: Rs. {surcharge}")
    print(f"Final Bill: Rs. {final_bill}")

# task2
matric_percentage = float(input("Enter Matric percentage: "))
fsc_percentage = float(input("Enter FSc percentage: "))
entry_test_percentage = float(input("Enter Entry Test percentage: "))
if matric_percentage < 50 or fsc_percentage < 50 or entry_test_percentage < 40:
    print("Rejected due to low scores.")
else:
    interview_score = float(input("Enter Interview score: "))
    final_score = (fsc_percentage * 0.40) + (entry_test_percentage * 0.40) + (interview_score * 0.20)

    if final_score < 0 or final_score > 100:
        print("Invalid final score.")
    elif final_score >= 90:
        category = "Full Scholarship"
    elif final_score >= 80:
        category = "Merit Admission"
    elif final_score >= 70:
        category = "Normal Admission"
    elif final_score >= 60:
        category = "Waiting List"
    else:
        category = "Rejected"

    print(f"Final Score: {final_score}")
    print(f"Admission Category: {category}")

# task 3
# ATM Transaction System
balance = float(input("Enter your current balance: Rs. "))
transaction_type = int(input("""
1 → Withdraw
2 → Deposit
3 → Check Balance

Enter transaction type: """))

amount = 0

if transaction_type == 1:

    amount = float(input("Enter withdrawal amount: Rs. "))

    if amount <= 0:
        print("Invalid amount. Amount must be positive.")

    elif amount % 500 != 0:
        print("Withdrawal amount must be a multiple of 500.")

    elif amount > balance:
        print("Insufficient balance.")

    elif balance - amount < 500:
        print("Transaction rejected.")
        print("Your balance cannot fall below Rs. 500.")

    else:
        balance -= amount

        print("\nWithdrawal successful!")
        print(f"Withdrawn: Rs. {amount}")
        print(f"Remaining Balance: Rs. {balance}")


elif transaction_type == 2:

    amount = float(input("Enter deposit amount: Rs. "))

    if amount <= 0:
        print("Invalid amount. Amount must be positive.")

    elif amount > 100000:
        print("Deposit rejected.")
        print("Maximum deposit allowed is Rs. 100,000.")

    else:
        balance += amount

        print("\nDeposit successful!")
        print(f"Deposited: Rs. {amount}")
        print(f"New Balance: Rs. {balance}")


elif transaction_type == 3:

    print(f"\nCurrent Balance: Rs. {balance}")


else:
    print("Invalid transaction type.")

# task 4
# Employee Salary & Tax Calculator

employee_name = input("Enter employee name: ")

basic_salary = float(input("Enter basic salary: Rs. "))

experience = int(input("Enter years of experience: "))

performance = float(input("Enter performance rating: "))


# Experience Bonus

if experience >= 5:
    experience_bonus_percent = 20

elif experience >= 3:
    experience_bonus_percent = 10

elif experience >= 1:
    experience_bonus_percent = 5

else:
    experience_bonus_percent = 0


# Performance Bonus

if performance >= 90:
    performance_bonus_percent = 15

elif performance >= 75:
    performance_bonus_percent = 10

elif performance >= 60:
    performance_bonus_percent = 5

else:
    performance_bonus_percent = 0


experience_bonus = basic_salary * experience_bonus_percent / 100

performance_bonus = basic_salary * performance_bonus_percent / 100

gross_salary = basic_salary + experience_bonus + performance_bonus


# Tax

if gross_salary <= 50000:
    tax_percent = 0

elif gross_salary <= 100000:
    tax_percent = 5

elif gross_salary <= 200000:
    tax_percent = 10

else:
    tax_percent = 15


tax = gross_salary * tax_percent / 100

final_salary = gross_salary - tax


print("\n========== SALARY REPORT ==========")

print(f"Employee: {employee_name}")
print(f"Basic Salary: Rs. {basic_salary}")
print(f"Experience Bonus: Rs. {experience_bonus}")
print(f"Performance Bonus: Rs. {performance_bonus}")
print(f"Gross Salary: Rs. {gross_salary}")
print(f"Tax: Rs. {tax}")
print(f"Final Salary: Rs. {final_salary}")

# task 5
# Smart Shipping Calculator
# Smart Shipping Calculator

order_amount = float(input("Enter order amount: Rs. "))

city = input("Enter your city: ").strip().lower()

customer_type = input(
    "Enter customer type (regular/premium/business): "
).strip().lower()

delivery_type = input(
    "Enter delivery type (standard/express): "
).strip().lower()


# Validate customer type

if customer_type != "regular" and \
   customer_type != "premium" and \
   customer_type != "business":

    print("Invalid customer type.")

else:

    # Validate delivery type

    if delivery_type != "standard" and delivery_type != "express":

        print("Invalid delivery type.")

    else:

        delivery_charge = 0


        # Standard Delivery

        if delivery_type == "standard":

            if customer_type == "premium":
                delivery_charge = 0

            elif customer_type == "regular":

                if order_amount >= 5000:
                    delivery_charge = 0
                else:
                    delivery_charge = 300

            elif customer_type == "business":

                if order_amount >= 3000:
                    delivery_charge = 0
                else:
                    delivery_charge = 150


        # Express Delivery

        elif delivery_type == "express":

            if customer_type == "premium":
                delivery_charge = 250
            else:
                delivery_charge = 500


        # City charges

        if city == "lahore":
            city_charge = 0

        elif city == "islamabad":
            city_charge = 100

        elif city == "karachi":
            city_charge = 200

        else:
            city_charge = 300


        delivery_charge += city_charge

        final_amount = order_amount + delivery_charge


        print("\n========== ORDER SUMMARY ==========")

        print(f"Order Amount: Rs. {order_amount}")
        print(f"Customer Type: {customer_type}")
        print(f"Delivery Type: {delivery_type}")
        print(f"City: {city}")
        print(f"Delivery Charges: Rs. {delivery_charge}")
        print(f"Final Amount: Rs. {final_amount}")

# a task for section 2 + section 3 all topics combined  for practice
# FINAL PROJECT — E-Commerce Order Management System

# This final task combines:

# list
# set
# dictionary
# List methods
# Set methods
# Dictionary methods
# if / elif / else
# User input
# Arithmetic operators
# Strings
# Type casting
# Starting data
# products = {
#     "laptop": {
#         "price": 120000,
#         "stock": 5,
#         "category": "electronics"
#     },
#     "phone": {
#         "price": 80000,
#         "stock": 10,
#         "category": "electronics"
#     },
#     "chair": {
#         "price": 15000,
#         "stock": 3,
#         "category": "furniture"
#     },
#     "table": {
#         "price": 25000,
#         "stock": 7,
#         "category": "furniture"
#     }
# }

# customers = {
#     "Ali": {
#         "type": "regular",
#         "orders": []
#     },
#     "Usman": {
#         "type": "premium",
#         "orders": []
#     },
#     "Ahmed": {
#         "type": "business",
#         "orders": []
#     }
# }

# categories = {
#     "electronics",
#     "furniture"
# }
# Your program should provide this menu
# ========== E-COMMERCE SYSTEM ==========

# 1. View Products
# 2. Search Product
# 3. Add Product
# 4. Remove Product
# 5. Update Stock
# 6. Place Order
# 7. View Customer Orders
# 8. Add Category
# 9. Remove Category
# 10. Inventory Report
# 11. Exit
# 1. View Products

# Display:

# Product
# Price
# Stock
# Category

# Use dictionary methods such as:

# .keys()
# .values()
# .items()
# 2. Search Product

# Ask the user for a product name.

# Use:

# .lower()
# .strip()
# in
# .get()

# If it exists, display its details.

# Otherwise:

# Product not found.
# 3. Add Product

# Ask the user for:

# Product name
# Price
# Stock
# Category

# Before adding:

# Check whether the product already exists.
# Check whether the category exists.
# Price cannot be negative.
# Stock cannot be negative.

# Use dictionary operations such as:

# products[name] = {...}
# 4. Remove Product

# Ask for the product name.

# If it exists:

# pop()

# Remove it.

# Otherwise display an error.

# 5. Update Stock

# Ask for:

# Product name
# New stock

# Validate the input using if / elif / else.

# 6. Place Order

# Ask:

# Customer name
# Product name
# Quantity

# Check:

# Does the customer exist?
# Does the product exist?
# Is quantity positive?
# Is enough stock available?

# Then calculate:

# subtotal = price × quantity

# Apply customer discount:

# Premium  → 10%
# Business → 15%
# Regular  → 0%

# Then calculate delivery:

# Subtotal >= 5000 → Free
# Otherwise:
#     Regular  → 300
#     Premium  → 0
#     Business → 150

# Finally:

# Final Amount = Discounted Subtotal + Delivery

# Update the product's stock.

# Store the order inside the customer's orders list.

# 7. View Customer Orders

# Ask for a customer name.

# Display every order stored in their list.

# For example:

# ========== ORDER HISTORY ==========

# Product: Laptop
# Quantity: 2
# Subtotal: Rs. 240000
# Discount: Rs. 24000
# Delivery: Free
# Final Amount: Rs. 216000
# 8. Add Category

# Ask for a category name.

# Add it to the set:

# categories.add()

# Before adding, check whether it already exists.

# 9. Remove Category

# Ask for a category.

# You should not allow removal if any product is currently using that category.

# This requires combining:

# set
# dictionary
# if / elif / else
# 10. Inventory Report

# Generate a report showing:

# Total Products
# Total Stock Units
# Total Inventory Value
# Most Expensive Product
# Product With Lowest Stock
# Available Categories

# For inventory value:

# price × stock

# Also create a list containing products whose stock is below 5:

# low_stock_products = []

# Then display a warning:

# WARNING: Low stock products
# 🎯 Main Challenge

# For the final project, don't use functions yet if you are currently practicing only these topics.

# Try to solve it using only:

# list
# set
# dictionary

# if
# elif
# else

# for / while        # if you have already learned loops

# and their built-in methods.


# ==========================================
# E-COMMERCE ORDER MANAGEMENT SYSTEM
# ==========================================


products = {
    "laptop": {
        "price": 120000,
        "stock": 5,
        "category": "electronics"
    },

    "phone": {
        "price": 80000,
        "stock": 10,
        "category": "electronics"
    },

    "chair": {
        "price": 15000,
        "stock": 3,
        "category": "furniture"
    },

    "table": {
        "price": 25000,
        "stock": 7,
        "category": "furniture"
    }
}


customers = {
    "Ali": {
        "type": "regular",
        "orders": []
    },

    "Usman": {
        "type": "premium",
        "orders": []
    },

    "Ahmed": {
        "type": "business",
        "orders": []
    }
}


categories = {
    "electronics",
    "furniture"
}


while True:

    print("""
=========================================
       E-COMMERCE MANAGEMENT SYSTEM
=========================================

1. View Products
2. Search Product
3. Add Product
4. Remove Product
5. Update Stock
6. Place Order
7. View Customer Orders
8. Add Category
9. Remove Category
10. Inventory Report
11. Exit

=========================================
""")

    choice = input("Enter your choice: ")


    # ==========================================
    # 1. VIEW PRODUCTS
    # ==========================================

    if choice == "1":

        print("\n========== PRODUCTS ==========")

        for name, details in products.items():

            print(f"""
Product  : {name}
Price    : Rs. {details['price']}
Stock    : {details['stock']}
Category : {details['category']}
""")


    # ==========================================
    # 2. SEARCH PRODUCT
    # ==========================================

    elif choice == "2":

        name = input("Enter product name: ").strip().lower()

        if name in products:

            product = products.get(name)

            print("\nProduct Found!")

            print(f"Name     : {name}")
            print(f"Price    : Rs. {product['price']}")
            print(f"Stock    : {product['stock']}")
            print(f"Category : {product['category']}")

        else:

            print("Product not found.")


    # ==========================================
    # 3. ADD PRODUCT
    # ==========================================

    elif choice == "3":

        name = input("Enter product name: ").strip().lower()

        if name in products:

            print("Product already exists.")

        else:

            price = float(input("Enter price: Rs. "))
            stock = int(input("Enter stock: "))
            category = input("Enter category: ").strip().lower()


            if price < 0:

                print("Price cannot be negative.")

            elif stock < 0:

                print("Stock cannot be negative.")

            elif category not in categories:

                print("Category does not exist.")

            else:

                products[name] = {
                    "price": price,
                    "stock": stock,
                    "category": category
                }

                print("Product added successfully.")


    # ==========================================
    # 4. REMOVE PRODUCT
    # ==========================================

    elif choice == "4":

        name = input("Enter product name: ").strip().lower()

        if name in products:

            products.pop(name)

            print("Product removed successfully.")

        else:

            print("Product not found.")


    # ==========================================
    # 5. UPDATE STOCK
    # ==========================================

    elif choice == "5":

        name = input("Enter product name: ").strip().lower()

        if name not in products:

            print("Product not found.")

        else:

            new_stock = int(input("Enter new stock: "))

            if new_stock < 0:

                print("Stock cannot be negative.")

            else:

                products[name]["stock"] = new_stock

                print("Stock updated successfully.")


    # ==========================================
    # 6. PLACE ORDER
    # ==========================================

    elif choice == "6":

        customer_name = input("Enter customer name: ").strip()

        product_name = input("Enter product name: ").strip().lower()

        quantity = int(input("Enter quantity: "))


        # Check customer

        if customer_name not in customers:

            print("Customer does not exist.")


        # Check product

        elif product_name not in products:

            print("Product does not exist.")


        # Check quantity

        elif quantity <= 0:

            print("Quantity must be positive.")


        else:

            product = products[product_name]

            customer = customers[customer_name]


            # Check stock

            if quantity > product["stock"]:

                print("Not enough stock available.")

            else:

                price = product["price"]

                subtotal = price * quantity


                # Customer discount

                if customer["type"] == "premium":

                    discount_percent = 10

                elif customer["type"] == "business":

                    discount_percent = 15

                else:

                    discount_percent = 0


                discount = subtotal * discount_percent / 100

                discounted_subtotal = subtotal - discount


                # Delivery

                if discounted_subtotal >= 5000:

                    delivery = 0

                elif customer["type"] == "premium":

                    delivery = 0

                elif customer["type"] == "business":

                    delivery = 150

                else:

                    delivery = 300


                final_amount = discounted_subtotal + delivery


                # Update stock

                product["stock"] -= quantity


                # Create order dictionary

                order = {
                    "product": product_name,
                    "quantity": quantity,
                    "subtotal": subtotal,
                    "discount": discount,
                    "delivery": delivery,
                    "final_amount": final_amount
                }


                # Add order to customer's list

                customer["orders"].append(order)


                print("\n========== ORDER SUCCESSFUL ==========")

                print(f"Customer       : {customer_name}")
                print(f"Product        : {product_name}")
                print(f"Quantity       : {quantity}")
                print(f"Subtotal       : Rs. {subtotal}")
                print(f"Discount       : Rs. {discount}")
                print(f"Delivery       : Rs. {delivery}")
                print(f"Final Amount   : Rs. {final_amount}")
                print(f"Remaining Stock: {product['stock']}")


    # ==========================================
    # 7. VIEW CUSTOMER ORDERS
    # ==========================================

    elif choice == "7":

        customer_name = input("Enter customer name: ").strip()


        if customer_name not in customers:

            print("Customer does not exist.")

        else:

            orders = customers[customer_name]["orders"]


            if len(orders) == 0:

                print("This customer has no orders.")

            else:

                print("\n========== ORDER HISTORY ==========")


                for order in orders:

                    print(f"""
Product      : {order['product']}
Quantity     : {order['quantity']}
Subtotal     : Rs. {order['subtotal']}
Discount     : Rs. {order['discount']}
Delivery     : Rs. {order['delivery']}
Final Amount : Rs. {order['final_amount']}
-------------------------------------
""")


    # ==========================================
    # 8. ADD CATEGORY
    # ==========================================

    elif choice == "8":

        category = input("Enter new category: ").strip().lower()


        if category in categories:

            print("Category already exists.")

        else:

            categories.add(category)

            print("Category added successfully.")


    # ==========================================
    # 9. REMOVE CATEGORY
    # ==========================================

    elif choice == "9":

        category = input("Enter category to remove: ").strip().lower()


        if category not in categories:

            print("Category does not exist.")

        else:

            category_in_use = False


            for product in products.values():

                if product["category"] == category:

                    category_in_use = True

                    break


            if category_in_use:

                print(
                    "Cannot remove category because "
                    "products are using it."
                )

            else:

                categories.remove(category)

                print("Category removed successfully.")


    # ==========================================
    # 10. INVENTORY REPORT
    # ==========================================

    elif choice == "10":

        total_products = len(products)

        total_stock = 0

        total_inventory_value = 0

        most_expensive_product = None

        lowest_stock_product = None

        low_stock_products = []


        for name, product in products.items():

            total_stock += product["stock"]


            inventory_value = (
                product["price"] * product["stock"]
            )

            total_inventory_value += inventory_value


            # Most expensive

            if (
                most_expensive_product is None
                or product["price"] >
                products[most_expensive_product]["price"]
            ):

                most_expensive_product = name


            # Lowest stock

            if (
                lowest_stock_product is None
                or product["stock"] <
                products[lowest_stock_product]["stock"]
            ):

                lowest_stock_product = name


            # Low stock

            if product["stock"] < 5:

                low_stock_products.append(name)


        print("\n========== INVENTORY REPORT ==========")

        print(f"Total Products       : {total_products}")
        print(f"Total Stock Units    : {total_stock}")
        print(
            f"Total Inventory Value: "
            f"Rs. {total_inventory_value}"
        )

        print(
            f"Most Expensive       : "
            f"{most_expensive_product}"
        )

        print(
            f"Lowest Stock         : "
            f"{lowest_stock_product}"
        )

        print(
            f"Categories           : "
            f"{categories}"
        )


        if len(low_stock_products) > 0:

            print("\n⚠ LOW STOCK PRODUCTS:")

            for product in low_stock_products:

                print(f"- {product}")

        else:

            print("\nNo low-stock products.")


    # ==========================================
    # 11. EXIT
    # ==========================================

    elif choice == "11":

        print("Thank you for using the system!")

        break


    # ==========================================
    # INVALID MENU OPTION
    # ==========================================

    else:

        print("Invalid choice. Please select 1–11.")