from products.product_service import product_menu
from users.user_service import user_menu
from customers.customer_service import customer_menu
from inventory.inventory_service import inventory_menu
from cart.cart_service import cart_menu
from orders.order_service import order_menu
from coupons.coupon_service import coupon_menu
from reports.report_service import report_menu


def main():

    while True:

        print("""
================================================
        BUSINESS MANAGEMENT SYSTEM
================================================

1. Product Management
2. User Management
3. Customer Management
4. Inventory Management
5. Cart Management
6. Order Management
7. Coupon Management
8. Reports
9. Exit

================================================
""")

        choice = input("Enter choice: ")

        if choice == "1":
            product_menu()

        elif choice == "2":
            user_menu()

        elif choice == "3":
            customer_menu()

        elif choice == "4":
            inventory_menu()

        elif choice == "5":
            cart_menu()

        elif choice == "6":
            order_menu()

        elif choice == "7":
            coupon_menu()

        elif choice == "8":
            report_menu()

        elif choice == "9":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()