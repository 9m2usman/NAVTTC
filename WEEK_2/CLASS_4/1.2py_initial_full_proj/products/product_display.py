def display_product(product):

    print(
        f"ID: {product['id']}\n"
        f"Name: {product['name']}\n"
        f"Category: {product['category']}\n"
        f"Price: {product['price']:.2f}\n"
        f"Stock: {product['stock']}"
    )


def display_products(products):

    if not products:
        print("No products found.")
        return

    print("-" * 75)

    print(
        f"{'ID':<8}"
        f"{'NAME':<20}"
        f"{'CATEGORY':<20}"
        f"{'PRICE':<12}"
        f"{'STOCK':<8}"
    )

    print("-" * 75)

    for product in products:
        print(
            f"{product['id']:<8}"
            f"{product['name']:<20}"
            f"{product['category']:<20}"
            f"{product['price']:<12.2f}"
            f"{product['stock']:<8}"
        )

    print("-" * 75)