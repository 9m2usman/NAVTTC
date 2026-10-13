from products.product_service import products, load_products

cart = []


def add_to_cart():
    product_id = int(input("Product ID: "))
    quantity = int(input("Quantity: "))

    product = next(
        (p for p in products if p["id"] == product_id),
        None
    )

    if not product:
        print("Product not found.")
        return

    if quantity <= 0:
        print("Invalid quantity.")
        return

    existing = next(
        (item for item in cart if item["product_id"] == product_id),
        None
    )

    current_quantity = existing["quantity"] if existing else 0

    if current_quantity + quantity > product["stock"]:
        print("Insufficient stock.")
        return

    if existing:
        existing["quantity"] += quantity
    else:
        cart.append({
            "product_id": product_id,
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        })

    print("Product added to cart.")


def view_cart():
    if not cart:
        print("Cart is empty.")
        return

    total = 0

    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal

        print(
            f"{item['name']} | "
            f"{item['quantity']} x "
            f"{item['price']} = {subtotal}"
        )

    print(f"\nTotal: Rs. {total:.2f}")


def remove_from_cart():
    product_id = int(input("Product ID: "))

    item = next(
        (i for i in cart if i["product_id"] == product_id),
        None
    )

    if item:
        cart.remove(item)
        print("Removed from cart.")
    else:
        print("Product not in cart.")


def get_total():
    return sum(
        item["price"] * item["quantity"]
        for item in cart
    )


def clear_cart():
    cart.clear()


def cart_menu():
    load_products()

    while True:
        print("""
========== CART ==========
1. Add Product
2. View Cart
3. Remove Product
4. Exit
""")

        choice = input("Choice: ")

        if choice == "1":
            add_to_cart()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")