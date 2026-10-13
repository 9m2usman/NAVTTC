from storage.file_handler import read_file, write_file

CUSTOMER_FILE = "data/customers.txt"
customers = []


def load_customers():
    global customers
    customers = []

    for line in read_file(CUSTOMER_FILE):
        parts = line.strip().split("|")

        if len(parts) == 4:
            customers.append({
                "id": int(parts[0]),
                "name": parts[1],
                "phone": parts[2],
                "email": parts[3]
            })


def save_customers():
    data = [
        f"{c['id']}|{c['name']}|{c['phone']}|{c['email']}\n"
        for c in customers
    ]

    write_file(CUSTOMER_FILE, data)


def add_customer():
    customer_id = int(input("Customer ID: "))

    if any(c["id"] == customer_id for c in customers):
        print("Customer ID already exists.")
        return

    customer = {
        "id": customer_id,
        "name": input("Name: "),
        "phone": input("Phone: "),
        "email": input("Email: ")
    }

    customers.append(customer)
    save_customers()

    print("Customer added successfully.")


def view_customers():
    if not customers:
        print("No customers found.")
        return

    for customer in customers:
        print(customer)


def search_customer():
    keyword = input("Search name/phone/email: ").lower()

    results = [
        c for c in customers
        if keyword in c["name"].lower()
        or keyword in c["phone"].lower()
        or keyword in c["email"].lower()
    ]

    for customer in results:
        print(customer)

    if not results:
        print("Customer not found.")


def delete_customer():
    customer_id = int(input("Customer ID: "))

    customer = next(
        (c for c in customers if c["id"] == customer_id),
        None
    )

    if customer:
        customers.remove(customer)
        save_customers()
        print("Customer deleted.")
    else:
        print("Customer not found.")


def customer_menu():
    load_customers()

    while True:
        print("""
========== CUSTOMER MANAGEMENT ==========
1. Add Customer
2. View Customers
3. Search Customer
4. Delete Customer
5. Exit
""")

        choice = input("Choice: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            search_customer()
        elif choice == "4":
            delete_customer()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")