# # 1. List — High-Level Task
# # Task: Student Performance Analyzer

# # Write a Python program that takes a list of student marks:

# # marks = [78, 92, 45, 88, 67, 92, 55, 39, 88, 71, 45]

# # The program should:

# # Display the highest and lowest marks.
# # Calculate the average.
# # Remove duplicate marks.
# # Sort the unique marks in descending order.
# # Count how many students scored:
# # 80 or above
# # 60–79
# # 40–59
# # below 40
# # Find the position/index of the first occurrence of the highest mark.
# # Add a new student's mark entered by the user.
# # Remove a mark entered by the user if it exists.
# # Display the final list.

marks = [78, 92, 45, 88, 67, 92, 55, 39, 88, 71, 45]
print(f"Highest marks in list : {max(marks)}\nLowest marks in list : {min(marks)}")
print(f"Average marks in list : {sum(marks) / len(marks)}")
marks = list(set(marks))
marks.sort(reverse=True)
print(f"Unique marks in descending order : {marks}")
sum1,sum2,sum3,sum4 = 0,0,0,0
for mark in marks:
    if mark >= 80:
        sum1+=marks.count(mark)
    elif mark >= 60:
        sum2+=marks.count(mark)
    elif mark >= 40:
        sum3+=marks.count(mark)
    else:
        sum4+=marks.count(mark)
print(f"Number of students scored 80 or above : {sum1}")
print(f"Number of students scored 60–79 : {sum2}")
print(f"Number of students scored 40–59 : {sum3}")
print(f"Number of students scored below 40 : {sum4}")
print(f"Positionn of 1st occurrence of highest mark : {marks.index(max(marks))}")
marks.append(int(input("enter new std marks : ")))
print(f"Final list of marks : {marks}")
mark_to_remove = int(input("enter mark to remove : "))
if mark_to_remove in marks:
    marks.remove(mark_to_remove)
    print(f"Final list of marks after removing {mark_to_remove} : {marks}")

       
# # 2. Set — High-Level Task
# # Task: Course Enrollment Analyzer

# # Three departments have students enrolled in different courses:

# # python_students = {"Ali", "Usman", "Ahmed", "Sara", "Hina", "Bilal"}
# # web_students = {"Usman", "Sara", "Hamza", "Hina", "Zain"}
# # ai_students = {"Ali", "Usman", "Hina", "Hamza", "Ayesha"}

# # Write a program that determines:

# # Students studying both Python and Web.
# # Students studying Python or Web but not both.
# # Students studying all three courses.
# # Students studying only AI.
# # Total number of unique students.
# # Students who are studying Python but not AI.
# # Add a new student to the AI course.
# # Remove a student from the Web course if they exist.
# # Check whether a student entered by the user is enrolled in AI.
# # Display all students alphabetically.

python_students = {"Ali", "Usman", "Ahmed", "Sara", "Hina", "Bilal"}
web_students = {"Usman", "Sara", "Hamza", "Hina", "Zain"}
ai_students = {"Ali", "Usman", "Hina", "Hamza", "Ayesha"}

python_web_students = python_students.intersection(web_students)
python_or_web_students = set()
for student in python_students.union(web_students):
    if student not in python_web_students:
        python_or_web_students.add(student)

python_web_ai_students = python_students.intersection(web_students).intersection(ai_students)
ai_only_students = ai_students.difference(python_students.union(web_students))

unique_students = python_students.union(web_students).union(ai_students)
python_not_ai_students = python_students.difference(ai_students)
student_to_add = ai_students.add(input("Enter a new student to add to the AI course: "))
student_to_remove = input("Enter a student to remove from the Web course: ")
if student_to_remove in web_students:
    web_students.remove(student_to_remove)
student_to_check = input("Enter a student to check if he is enrolled in AI : ")
if student_to_check in ai_students:
    print(f"{student_to_check} is enrolled in AI.")
else:
    print(f"{student_to_check} is not enrolled in AI.")

print(f"Students studying both Python and Web: {python_web_students}")
print(f"Students studying Python or Web but not both: {python_or_web_students}")
print(f"Students studying all three courses: {python_web_ai_students}")
print(f"Students studying only AI: {ai_only_students}")
print(f"Total number of unique students: {len(unique_students)}")
print(f"Students studying Python but not AI: {python_not_ai_students}") 
studnets_alphabetically = sorted(unique_students)
print(f"All students alphabetically: {studnets_alphabetically}")


# 3. Dictionary — High-Level Task
# Task: E-Commerce Inventory Manager

# Create a dictionary:

# products = {
#     "laptop": {
#         "price": 120000,
#         "stock": 5,
#         "category": "electronics"
#     },
#     "phone": {
#         "price": 80000,
#         "stock": 10,
#         "category": "electronics"
#     },
#     "chair": {
#         "price": 15000,
#         "stock": 3,
#         "category": "furniture"
#     }
# }

# Your program should:

# Display all products.
# Display only products whose stock is greater than 5.
# Calculate the total inventory value:
# price × stock

# for every product.
# 4. Find the most expensive product.
# 5. Find the product with the lowest stock.
# 6. Allow the user to search for a product.
# 7. Allow the user to add a new product.
# 8. Allow the user to update the stock of an existing product.
# 9. Delete a product entered by the user.
# 10. Display all product names alphabetically.

products = {
    "laptop": {
        "price": 120000,
        "stock": 5,
        "category": "electronics"
    },
    "phone": {
        "price": 80000,
        "stock": 10,
        "category": "electronics"
    },
    "chair": {
        "price": 15000,
        "stock": 3,
        "category": "furniture"
    }
}

# simple using print or using loop to display them one by one
print("All products:", products) 
for product, details in products.items():
    print(f"{product}: {details}")

# stock greater than 5
for product, details in products.items():
    if details["stock"] > 5:
        print(f"{product}: {details}")

for details in products.values():
    total_inventory_value = details["price"] * details["stock"]
print(f"Total inventory value: {total_inventory_value}")

for product, details in products.items():
    for p in products.values():
        if details["price"] > p["price"]:
            most_expensive_product = product
print(f"Most expensive product: {most_expensive_product} with price {products[most_expensive_product]['price']}")

for product, details in products.items():
    for p in products.values():
        if details["stock"] < p["stock"]:
            lowest_stock_product = product
print(f"Product with lowest stock: {lowest_stock_product} with stock {products[lowest_stock_product]['stock']}")