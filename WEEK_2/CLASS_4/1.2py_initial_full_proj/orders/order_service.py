from storage.file_handler import read_file, write_file
from cart.cart_service import cart, get_total, clear_cart
from products.product_service import products, save_products

ORDER_FILE = "data/orders.txt"


def create_order():
    if not cart:
        print("Cart is empty.")
        return

    total = get_total()

    customer_id = int(input("Customer ID: "))

    order_id = len(read_file(ORDER_FILE)) + 1

    order = {
        "id": order_id,
        "customer_id": customer_id,
        "total": total
    }

    with open(ORDER_FILE, "a") as file:
        file.write(
            f"{order_id}|{customer_id}|{total}\n"
        )

    for item in cart:
        product = next(
            p for p in products
            if p["id"] == item["product_id"]
        )

        product["stock"] -= item["quantity"]

    save_products()

    print(f"""
========== ORDER CREATED ==========
Order ID: {order_id}
Customer ID: {customer_id}
Total: Rs. {total:.2f}
===================================
""")

    clear_cart()


def view_orders():
    orders = read_file(ORDER_FILE)

    if not orders:
        print("No orders found.")
        return

    for line in orders:
        print(line.strip())


def order_menu():
    while True:
        print("""
========== ORDERS ==========
1. Create Order
2. View Orders
3. Exit
""")

        choice = input("Choice: ")

        if choice == "1":
            create_order()
        elif choice == "2":
            view_orders()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")