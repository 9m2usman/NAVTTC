def format_currency(amount):
    return f"Rs. {amount:,.2f}"


def format_number(number):
    return f"{number:,}"


def print_header(title):
    width = 50

    print("\n" + "=" * width)
    print(title.center(width))
    print("=" * width)


def print_line(width=50):
    print("-" * width)


def format_product(product):
    return (
        f"ID: {product['id']} | "
        f"Name: {product['name']} | "
        f"Category: {product['category']} | "
        f"Price: {format_currency(product['price'])} | "
        f"Stock: {product['stock']}"
    )


def format_order(order):
    return (
        f"Order ID: {order['id']} | "
        f"Customer ID: {order['customer_id']} | "
        f"Total: {format_currency(order['total'])}"
    )