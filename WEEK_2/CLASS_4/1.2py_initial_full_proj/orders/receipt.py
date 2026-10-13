from cart.cart_service import cart, get_total


def print_receipt():
    print("\n========== RECEIPT ==========")

    for item in cart:
        subtotal = item["price"] * item["quantity"]

        print(
            f"{item['name']} | "
            f"{item['quantity']} x "
            f"{item['price']} = "
            f"{subtotal}"
        )

    print("------------------------------")
    print(f"TOTAL: Rs. {get_total():.2f}")
    print("==============================")