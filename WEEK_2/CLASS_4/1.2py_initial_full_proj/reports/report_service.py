from products.product_service import products, load_products
from storage.file_handler import read_file


def sales_report():
    orders = read_file("data/orders.txt")

    total_sales = 0

    for order in orders:
        parts = order.strip().split("|")

        if len(parts) == 3:
            total_sales += float(parts[2])

    print("\n========== SALES REPORT ==========")
    print(f"Total Orders: {len(orders)}")
    print(f"Total Sales: Rs. {total_sales:.2f}")


def inventory_report():
    load_products()

    print("\n========== INVENTORY REPORT ==========")

    print(f"Total Products: {len(products)}")

    total_stock = sum(
        p["stock"] for p in products
    )

    print(f"Total Stock Units: {total_stock}")

    low_stock = [
        p for p in products
        if p["stock"] <= 5
    ]

    print(f"Low Stock Products: {len(low_stock)}")


def report_menu():

    while True:
        print("""
========== REPORTS ==========
1. Sales Report
2. Inventory Report
3. Exit
""")

        choice = input("Choice: ")

        if choice == "1":
            sales_report()

        elif choice == "2":
            inventory_report()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")