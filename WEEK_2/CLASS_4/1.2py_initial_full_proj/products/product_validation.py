def validate_id(product_id):
    return product_id > 0


def validate_name(name):
    return bool(name.strip())


def validate_category(category):
    return bool(category.strip())


def validate_price(price):
    return price > 0


def validate_stock(stock):
    return stock >= 0