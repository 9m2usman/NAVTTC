from products.product_service import products, load_products, save_products


def increase_stock():
    product_id = int(input("Product ID: "))
    quantity = int(input("Quantity to add: "))

    product = next(
        (p for p in products if p["id"] == product_id),
        None
    )

    if not product:
        print("Product not found.")
        return

    if quantity <= 0:
        print("Quantity must be positive.")
        return

    product["stock"] += quantity
    save_products()

    print(f"Stock updated. New stock: {product['stock']}")


def decrease_stock():
    product_id = int(input("Product ID: "))
    quantity = int(input("Quantity to remove: "))

    product = next(
        (p for p in products if p["id"] == product_id),
        None
    )

    if not product:
        print("Product not found.")
        return

    if quantity <= 0:
        print("Quantity must be positive.")
        return

    if quantity > product["stock"]:
        print("Insufficient stock.")
        return

    product["stock"] -= quantity
    save_products()

    print(f"Stock updated. New stock: {product['stock']}")


def low_stock():
    limit = int(input("Low-stock limit: "))

    result = [
        p for p in products
        if p["stock"] <= limit
    ]

    if not result:
        print("No low-stock products.")
        return

    for product in result:
        print(product)


def inventory_menu():
    load_products()

    while True:
        print("""
========== INVENTORY ==========
1. Increase Stock
2. Decrease Stock
3. Low Stock Products
4. Exit
""")

        choice = input("Choice: ")

        if choice == "1":
            increase_stock()
        elif choice == "2":
            decrease_stock()
        elif choice == "3":
            low_stock()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")