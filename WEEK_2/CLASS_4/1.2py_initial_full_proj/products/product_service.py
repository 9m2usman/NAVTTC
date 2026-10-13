from storage.file_handler import read_file, write_file

PRODUCT_FILE = "data/products.txt"

products = []


def load_products():
    global products

    products = []

    data = read_file(PRODUCT_FILE)

    for line in data:
        line = line.strip()

        if not line:
            continue

        parts = line.split("|")

        if len(parts) == 5:
            product = {
                "id": int(parts[0]),
                "name": parts[1],
                "category": parts[2],
                "price": float(parts[3]),
                "stock": int(parts[4])
            }

            products.append(product)


def save_products():
    data = []

    for product in products:
        line = (
            f"{product['id']}|"
            f"{product['name']}|"
            f"{product['category']}|"
            f"{product['price']}|"
            f"{product['stock']}\n"
        )

        data.append(line)

    write_file(PRODUCT_FILE, data)


def add_product():
    print("\n========== ADD PRODUCT ==========")

    product_id = int(input("Product ID: "))

    for product in products:
        if product["id"] == product_id:
            print("Product ID already exists.")
            return

    name = input("Product Name: ")
    category = input("Category: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))

    product = {
        "id": product_id,
        "name": name,
        "category": category,
        "price": price,
        "stock": stock
    }

    products.append(product)
    save_products()

    print("Product added successfully.")


def view_products(product_list=None):

    if product_list is None:
        product_list = products

    if not product_list:
        print("\nNo products found.")
        return

    print("\n" + "-" * 75)
    print(
        f"{'ID':<8}"
        f"{'NAME':<20}"
        f"{'CATEGORY':<20}"
        f"{'PRICE':<12}"
        f"{'STOCK':<8}"
    )
    print("-" * 75)

    for product in product_list:
        print(
            f"{product['id']:<8}"
            f"{product['name']:<20}"
            f"{product['category']:<20}"
            f"{product['price']:<12.2f}"
            f"{product['stock']:<8}"
        )

    print("-" * 75)


def search_product():

    print("""
1. Search by ID
2. Search by Name
3. Search by Category
""")

    choice = input("Choice: ")

    if choice == "1":
        product_id = int(input("Product ID: "))

        result = [
            p for p in products
            if p["id"] == product_id
        ]

    elif choice == "2":
        name = input("Product name: ").lower()

        result = [
            p for p in products
            if name in p["name"].lower()
        ]

    elif choice == "3":
        category = input("Category: ").lower()

        result = [
            p for p in products
            if category in p["category"].lower()
        ]

    else:
        print("Invalid choice.")
        return

    view_products(result)


def update_product():

    product_id = int(input("Enter Product ID: "))

    product = next(
        (p for p in products if p["id"] == product_id),
        None
    )

    if product is None:
        print("Product not found.")
        return

    print("""
1. Name
2. Category
3. Price
4. Stock
5. All
""")

    choice = input("Choice: ")

    if choice == "1":
        product["name"] = input("New name: ")

    elif choice == "2":
        product["category"] = input("New category: ")

    elif choice == "3":
        product["price"] = float(input("New price: "))

    elif choice == "4":
        product["stock"] = int(input("New stock: "))

    elif choice == "5":
        product["name"] = input("New name: ")
        product["category"] = input("New category: ")
        product["price"] = float(input("New price: "))
        product["stock"] = int(input("New stock: "))

    else:
        print("Invalid choice.")
        return

    save_products()

    print("Product updated successfully.")


def delete_product():

    product_id = int(input("Product ID: "))

    for product in products:

        if product["id"] == product_id:
            products.remove(product)
            save_products()

            print("Product deleted successfully.")
            return

    print("Product not found.")


def filter_products():

    print("""
1. Below Price
2. Above Price
3. Category
4. Low Stock
""")

    choice = input("Choice: ")

    if choice == "1":
        price = float(input("Price: "))

        result = [
            p for p in products
            if p["price"] < price
        ]

    elif choice == "2":
        price = float(input("Price: "))

        result = [
            p for p in products
            if p["price"] > price
        ]

    elif choice == "3":
        category = input("Category: ").lower()

        result = [
            p for p in products
            if p["category"].lower() == category
        ]

    elif choice == "4":
        stock = int(input("Maximum stock: "))

        result = [
            p for p in products
            if p["stock"] < stock
        ]

    else:
        print("Invalid choice.")
        return

    view_products(result)


def sort_products():

    print("""
1. Price Low → High
2. Price High → Low
3. Name A → Z
4. Stock Low → High
""")

    choice = input("Choice: ")

    if choice == "1":
        result = sorted(
            products,
            key=lambda p: p["price"]
        )

    elif choice == "2":
        result = sorted(
            products,
            key=lambda p: p["price"],
            reverse=True
        )

    elif choice == "3":
        result = sorted(
            products,
            key=lambda p: p["name"].lower()
        )

    elif choice == "4":
        result = sorted(
            products,
            key=lambda p: p["stock"]
        )

    else:
        print("Invalid choice.")
        return

    view_products(result)


def product_menu():

    load_products()

    while True:

        print("""
========================================
          PRODUCT MANAGEMENT
========================================

1. Add Product
2. View Products
3. Search Product
4. Update Product
5. Delete Product
6. Filter Products
7. Sort Products
8. Exit

========================================
""")

        choice = input("Enter choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            filter_products()

        elif choice == "7":
            sort_products()

        elif choice == "8":
            break

        else:
            print("Invalid choice.")