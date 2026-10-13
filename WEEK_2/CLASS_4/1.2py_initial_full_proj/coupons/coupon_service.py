from storage.file_handler import read_file, write_file

COUPON_FILE = "data/coupons.txt"
coupons = []


def load_coupons():
    global coupons
    coupons = []

    for line in read_file(COUPON_FILE):
        parts = line.strip().split("|")

        if len(parts) == 3:
            coupons.append({
                "code": parts[0],
                "discount": float(parts[1]),
                "active": parts[2]
            })


def save_coupons():
    data = [
        f"{c['code']}|{c['discount']}|{c['active']}\n"
        for c in coupons
    ]

    write_file(COUPON_FILE, data)


def add_coupon():
    code = input("Coupon code: ").upper()

    if any(c["code"] == code for c in coupons):
        print("Coupon already exists.")
        return

    discount = float(input("Discount percentage: "))

    if not 0 < discount <= 100:
        print("Invalid discount.")
        return

    coupons.append({
        "code": code,
        "discount": discount,
        "active": "yes"
    })

    save_coupons()

    print("Coupon created.")


def view_coupons():
    for coupon in coupons:
        print(coupon)


def coupon_menu():
    load_coupons()

    while True:
        print("""
========== COUPONS ==========
1. Add Coupon
2. View Coupons
3. Exit
""")

        choice = input("Choice: ")

        if choice == "1":
            add_coupon()
        elif choice == "2":
            view_coupons()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")