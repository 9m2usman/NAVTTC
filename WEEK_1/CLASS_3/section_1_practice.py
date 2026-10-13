"""
PYTHON HIGH-LEVEL PRACTICE TASKS
================================

Topics covered:
1. Variables
2. Data Types
3. Strings + String Functions
4. Conditional Operators / Conditional Statements
5. Arithmetic Operators
6. Type Casting
7. f-strings (Python's formatted string literals)
8. input() function
9. Two final integrated tasks using ALL topics

For EVERY task:
- Method 1 = Optimized / clean / practical solution
- Method 2 = Non-optimized

Important:
These solutions are intentionally different. Method 2 is included to help
understand how the same problem can be solved less efficiently.
"""

# ================================================================
# TOPIC 1: VARIABLES
# ================================================================
# TASK 1:
# Build a student result record using variables.
# Store name, roll number, three subject marks, total marks, percentage,
# and pass/fail status. Display the complete record.

# ---------------- METHOD 1: OPTIMIZED ----------------
name = "Usman"
roll_no = 101
math = 88
english = 79
computer = 94

total = math + english + computer
percentage = total / 300 * 100
status = "PASS" if percentage >= 40 else "FAIL"

print("\n--- Variables Task 1 / Optimized ---")
print(name, roll_no, total, percentage, status)

# ---------------- METHOD 2: NON-OPTIMIZED ----------------
student_name = "Usman"
student_roll = 101
math_marks = 88
english_marks = 79
computer_marks = 94

student_total = math_marks+english_marks+computer_marks
student_percentage = (student_total / 300) * 100

if student_percentage >= 40:
    student_status = "PASS"
else:
    student_status = "FAIL"

print("\n--- Variables Task 1 / Non-Optimized ---")
print("Name:", student_name)
print("Roll:", student_roll)
print("Math:", math_marks)
print("English:", english_marks)
print("Computer:", computer_marks)
print("Total:", student_total)
print("Percentage:", student_percentage)
print("Status:", student_status)


# TASK 2:
# Create variables for an employee: name, department, monthly salary,
# years of experience and bonus percentage. Calculate annual salary
# including the bonus.

# ---------------- METHOD 1: OPTIMIZED ----------------
employee = "Ali"
department = "IT"
monthly_salary = 85000
experience = 3
bonus_percent = 10

annual_salary = monthly_salary * 12
bonus = annual_salary * bonus_percent / 100
final_annual_salary = annual_salary + bonus

print("\n--- Variables Task 2 / Optimized ---")
print(employee, department, experience, final_annual_salary)

# ---------------- METHOD 2: NON-OPTIMIZED ----------------
employee_name = "Ali"
employee_department = "IT"
salary_per_month = 85000
experience_years = 3
bonus_rate = 10

salary_jan = salary_per_month
salary_feb = salary_per_month
salary_mar = salary_per_month
salary_apr = salary_per_month
salary_may = salary_per_month
salary_jun = salary_per_month
salary_jul = salary_per_month
salary_aug = salary_per_month
salary_sep = salary_per_month
salary_oct = salary_per_month
salary_nov = salary_per_month
salary_dec = salary_per_month

year_salary = (
    salary_jan + salary_feb + salary_mar + salary_apr +
    salary_may + salary_jun + salary_jul + salary_aug +
    salary_sep + salary_oct + salary_nov + salary_dec
)

bonus_amount = year_salary * bonus_rate / 100
complete_salary = year_salary + bonus_amount

print("\n--- Variables Task 2 / Non-Optimized ---")
print("Employee:", employee_name)
print("Department:", employee_department)
print("Experience:", experience_years)
print("Annual salary:", complete_salary)


# ================================================================
# TOPIC 2: DATA TYPES
# ================================================================
# TASK 1:
# Create one example of each major basic Python data type:
# int, float, str, bool, list, tuple, set and dict.
# Display the value and its type.

# ---------------- METHOD 1: OPTIMIZED ----------------
values = [
    25,
    92.5,
    "Python",
    True,
    [10, 20, 30],
    ("A", "B", "C"),
    {"Python", "Java"},
    {"name": "Usman", "age": 24}
]

print("\n--- Data Types Task 1 / Optimized ---")
for value in values:
    print(value, "->", type(value).__name__)

# ---------------- METHOD 2: NON-OPTIMIZED ----------------
number = 25
decimal_number = 92.5
language = "Python"
is_learning = True
marks = [10, 20, 30]
subjects = ("A", "B", "C")
languages = {"Python", "Java"}
person = {"name": "Usman", "age": 24}

print("\n--- Data Types Task 1 / Non-Optimized ---")
print(number, type(number))
print(decimal_number, type(decimal_number))
print(language, type(language))
print(is_learning, type(is_learning))
print(marks, type(marks))
print(subjects, type(subjects))
print(languages, type(languages))
print(person, type(person))


# TASK 2:
# Given mixed values, determine how many values are integers, floats,
# strings and booleans. Do not confuse bool with int.

# ---------------- METHOD 1: OPTIMIZED ----------------
mixed_values = [10, 5.5, "Python", True, 20, False, "AI", 9.8, 50]

counts = {"int": 0, "float": 0, "str": 0, "bool": 0}

for value in mixed_values:
    if type(value) is int:
        counts["int"] += 1
    elif type(value) is float:
        counts["float"] += 1
    elif type(value) is str:
        counts["str"] += 1
    elif type(value) is bool:
        counts["bool"] += 1

print("\n--- Data Types Task 2 / Optimized ---")
print(counts)

# ---------------- METHOD 2: NON-OPTIMIZED ----------------
int_count = 0
float_count = 0
string_count = 0
bool_count = 0

for value in mixed_values:
    if type(value) is int:
        int_count = int_count + 1

for value in mixed_values:
    if type(value) is float:
        float_count = float_count + 1

for value in mixed_values:
    if type(value) is str:
        string_count = string_count + 1

for value in mixed_values:
    if type(value) is bool:
        bool_count = bool_count + 1

print("\n--- Data Types Task 2 / Non-Optimized ---")
print("Integers:", int_count)
print("Floats:", float_count)
print("Strings:", string_count)
print("Booleans:", bool_count)


# ================================================================
# TOPIC 3: STRINGS + STRING FUNCTIONS
# ================================================================
# TASK 1:
# Take a messy product name and normalize it.
# Required operations: strip spaces, lower(), upper(), title(),
# replace(), split(), and count().

# ---------------- METHOD 1: OPTIMIZED ----------------
product_name = "   gaming LAPTOP - HP Victus   "

clean_name = product_name.strip()
lower_name = clean_name.lower()
upper_name = clean_name.upper()
title_name = clean_name.title()
hyphen_fixed = clean_name.replace("-", " ")
words = hyphen_fixed.split()
laptop_count = lower_name.count("laptop")

print("\n--- Strings Task 1 / Optimized ---")
print("Original:", product_name)
print("Lower:", lower_name)
print("Upper:", upper_name)
print("Title:", title_name)
print("Words:", words)
print("Laptop count:", laptop_count)

# ---------------- METHOD 2: NON-OPTIMIZED ----------------
raw_product = "   gaming LAPTOP - HP Victus   "
step1 = raw_product.strip()
step2 = step1.lower()
step3 = step2.upper()
step4 = step1.title()
step5 = step1.replace("-", " ")
step6 = step5.split(" ")
step7 = step2.count("laptop")

print("\n--- Strings Task 1 / Non-Optimized ---")
print("Original:", raw_product)
print("Step 1:", step1)
print("Step 2:", step2)
print("Step 3:", step3)
print("Step 4:", step4)
print("Step 5:", step5)
print("Step 6:", step6)
print("Laptop count:", step7)


# TASK 2:
# Analyze a sentence.
# Find its length, number of words, first and last character,
# number of vowels, and whether it starts/ends with specific text.

# ---------------- METHOD 1: OPTIMIZED ----------------
sentence = "Python programming makes problem solving powerful"

words = sentence.split()
vowels = "aeiou"
vowel_count = sum(1 for char in sentence.lower() if char in vowels)

print("\n--- Strings Task 2 / Optimized ---")
print("Length:", len(sentence))
print("Words:", len(words))
print("First character:", sentence[0])
print("Last character:", sentence[-1])
print("Vowels:", vowel_count)
print("Starts with Python:", sentence.startswith("Python"))
print("Ends with powerful:", sentence.endswith("powerful"))

# ---------------- METHOD 2: NON-OPTIMIZED ----------------
sentence2 = "Python programming makes problem solving powerful"
word_list = sentence2.split(" ")

count_vowels = 0
for character in sentence2:
    if (
        character == "a" or character == "e" or
        character == "i" or character == "o" or
        character == "u" or character == "A" or
        character == "E" or character == "I" or
        character == "O" or character == "U"
    ):
        count_vowels += 1

starts = False
ends = False

if sentence2[:6] == "Python":
    starts = True

if sentence2[-8:] == "powerful":
    ends = True

print("\n--- Strings Task 2 / Non-Optimized ---")
print("Length:", len(sentence2))
print("Words:", len(word_list))
print("First character:", sentence2[0])
print("Last character:", sentence2[len(sentence2) - 1])
print("Vowels:", count_vowels)
print("Starts with Python:", starts)
print("Ends with powerful:", ends)


# ================================================================
# TOPIC 4: CONDITIONAL OPERATORS / CONDITIONAL STATEMENTS
# ================================================================
# TASK 1:
# A university has these admission rules:
# - percentage >= 80: Excellent
# - percentage >= 70: Very Good
# - percentage >= 60: Good
# - percentage >= 50: Average
# - below 50: Not Eligible
# Also reject percentages below 0 or above 100.

# ---------------- METHOD 1: OPTIMIZED ----------------
percentage = 76

if percentage < 0 or percentage > 100:
    result = "Invalid percentage"
elif percentage >= 80:
    result = "Excellent"
elif percentage >= 70:
    result = "Very Good"
elif percentage >= 60:
    result = "Good"
elif percentage >= 50:
    result = "Average"
else:
    result = "Not Eligible"

print("\n--- Conditional Task 1 / Optimized ---")
print(result)

# ---------------- METHOD 2: NON-OPTIMIZED ----------------
percentage2 = 76

if percentage2 >= 0 and percentage2 <= 100:
    if percentage2 >= 80:
        result2 = "Excellent"
    else:
        if percentage2 >= 70:
            result2 = "Very Good"
        else:
            if percentage2 >= 60:
                result2 = "Good"
            else:
                if percentage2 >= 50:
                    result2 = "Average"
                else:
                    result2 = "Not Eligible"
else:
    result2 = "Invalid percentage"

print("\n--- Conditional Task 1 / Non-Optimized ---")
print(result2)


# TASK 2:
# Build a security/access decision.
# A user gets access only if:
# age >= 18, account is active, and either the role is admin
# or the user has paid.
# Produce a clear decision message.

# ---------------- METHOD 1: OPTIMIZED ----------------
age = 21
account_active = True
role = "user"
has_paid = True

if age >= 18 and account_active and (role == "admin" or has_paid):
    access = "ACCESS GRANTED"
else:
    access = "ACCESS DENIED"

print("\n--- Conditional Task 2 / Optimized ---")
print(access)

# ---------------- METHOD 2: NON-OPTIMIZED ----------------
age2 = 21
account_active2 = True
role2 = "user"
has_paid2 = True

if age2 >= 18:
    if account_active2:
        if role2 == "admin":
            access2 = "ACCESS GRANTED"
        else:
            if has_paid2:
                access2 = "ACCESS GRANTED"
            else:
                access2 = "ACCESS DENIED"
    else:
        access2 = "ACCESS DENIED"
else:
    access2 = "ACCESS DENIED"

print("\n--- Conditional Task 2 / Non-Optimized ---")
print(access2)


# ================================================================
# TOPIC 5: ARITHMETIC OPERATORS
# ================================================================
# TASK 1:
# A shop sells a laptop.
# Calculate subtotal, discount, tax, delivery charge, and final bill.
# Use +, -, *, /, //, %, and ** somewhere in the calculation/explanation.

# ---------------- METHOD 1: OPTIMIZED ----------------
price = 125000
quantity = 2
discount_rate = 10
tax_rate = 5
delivery = 1500

subtotal = price * quantity
discount = subtotal * discount_rate / 100
after_discount = subtotal - discount
tax = after_discount * tax_rate / 100
final_bill = after_discount + tax + delivery

print("\n--- Arithmetic Task 1 / Optimized ---")
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Tax:", tax)
print("Delivery:", delivery)
print("Final bill:", final_bill)
print("Integer division example:", final_bill // 1000)
print("Remainder example:", final_bill % 1000)
print("Power example:", 2 ** 3)

# ---------------- METHOD 2: NON-OPTIMIZED ----------------
item_price = 125000
items = 2
discount_percentage = 10
tax_percentage = 5
shipping = 1500

item_total = item_price * items
discount_part = item_total / 100
discount_amount = discount_part * discount_percentage
remaining_after_discount = item_total - discount_amount

tax_part = remaining_after_discount / 100
tax_amount = tax_part * tax_percentage

bill_before_shipping = remaining_after_discount + tax_amount
complete_bill = bill_before_shipping + shipping

print("\n--- Arithmetic Task 1 / Non-Optimized ---")
print("Subtotal:", item_total)
print("Discount:", discount_amount)
print("Tax:", tax_amount)
print("Final bill:", complete_bill)
print("Thousands:", complete_bill // 1000)
print("Remaining:", complete_bill % 1000)
print("2 squared:", 2 ** 2)


# TASK 2:
# Convert a total number of seconds into days, hours, minutes and seconds.
# Use // and % correctly.

# ---------------- METHOD 1: OPTIMIZED ----------------
total_seconds = 987654

days = total_seconds // 86400
remaining = total_seconds % 86400
hours = remaining // 3600
remaining %= 3600
minutes = remaining // 60
seconds = remaining % 60

print("\n--- Arithmetic Task 2 / Optimized ---")
print(days, "days,", hours, "hours,", minutes, "minutes,", seconds, "seconds")

# ---------------- METHOD 2: NON-OPTIMIZED ----------------
seconds_total = 987654

day_seconds = 24 * 60 * 60
hour_seconds = 60 * 60
minute_seconds = 60

days2 = seconds_total // day_seconds
after_days = seconds_total - (days2 * day_seconds)

hours2 = after_days // hour_seconds
after_hours = after_days - (hours2 * hour_seconds)

minutes2 = after_hours // minute_seconds
seconds2 = after_hours - (minutes2 * minute_seconds)

print("\n--- Arithmetic Task 2 / Non-Optimized ---")
print(days2, "days,", hours2, "hours,", minutes2, "minutes,", seconds2, "seconds")


# ================================================================
# TOPIC 6: TYPE CASTING
# ================================================================
# TASK 1:
# Convert string values representing marks into integers/floats.
# Calculate total and percentage and display the correct types.

# ---------------- METHOD 1: OPTIMIZED ----------------
math_text = "87"
english_text = "78"
computer_text = "92"

math_mark = int(math_text)
english_mark = int(english_text)
computer_mark = int(computer_text)

total_marks = math_mark + english_mark + computer_mark
percentage = float(total_marks) / 300 * 100

print("\n--- Type Casting Task 1 / Optimized ---")
print("Total:", total_marks, type(total_marks))
print("Percentage:", percentage, type(percentage))

# ---------------- METHOD 2: NON-OPTIMIZED ----------------
math_text2 = "87"
english_text2 = "78"
computer_text2 = "92"

m1 = int(math_text2)
m2 = int(english_text2)
m3 = int(computer_text2)

m1_float = float(m1)
m2_float = float(m2)
m3_float = float(m3)

total2 = m1 + m2 + m3
percentage2 = (m1_float + m2_float + m3_float) / float(300) * float(100)

print("\n--- Type Casting Task 1 / Non-Optimized ---")
print("Total:", total2, type(total2))
print("Percentage:", percentage2, type(percentage2))


# TASK 2:
# Given a string containing a price and quantity, convert them into
# appropriate numeric types and calculate the total cost.

# ---------------- METHOD 1: OPTIMIZED ----------------
price_text = "2499.50"
quantity_text = "4"

price_value = float(price_text)
quantity_value = int(quantity_text)

total_cost = price_value * quantity_value

print("\n--- Type Casting Task 2 / Optimized ---")
print("Total cost:", total_cost)

# ---------------- METHOD 2: NON-OPTIMIZED ----------------
price_text2 = "2499.50"
quantity_text2 = "4"

price_as_string = price_text2
quantity_as_string = quantity_text2

price_number = float(price_as_string)
quantity_number = int(quantity_as_string)

single_item_cost = price_number
total_cost2 = single_item_cost * quantity_number

print("\n--- Type Casting Task 2 / Non-Optimized ---")
print("Single item:", single_item_cost)
print("Quantity:", quantity_number)
print("Total cost:", total_cost2)


# ================================================================
# TOPIC 7: f-STRINGS / TEMPLATE LITERALS
# ================================================================
# TASK 1:
# Create a professional invoice using f-strings.
# Show customer name, product, quantity, unit price, subtotal,
# discount and final amount.

# ---------------- METHOD 1: OPTIMIZED ----------------
customer = "Usman"
product = "Mechanical Keyboard"
qty = 2
unit_price = 4500
discount = 500

subtotal = qty * unit_price
final_amount = subtotal - discount

invoice = (
    f"Customer: {customer}\n"
    f"Product: {product}\n"
    f"Quantity: {qty}\n"
    f"Unit Price: Rs. {unit_price:,.2f}\n"
    f"Subtotal: Rs. {subtotal:,.2f}\n"
    f"Discount: Rs. {discount:,.2f}\n"
    f"Final Amount: Rs. {final_amount:,.2f}"
)

print("\n--- f-string Task 1 / Optimized ---")
print(invoice)

# ---------------- METHOD 2: NON-OPTIMIZED ----------------
customer2 = "Usman"
product2 = "Mechanical Keyboard"
quantity2 = 2
price2 = 4500
discount2 = 500

line1 = f"Customer: {customer2}"
line2 = f"Product: {product2}"
line3 = f"Quantity: {quantity2}"
line4 = f"Unit Price: Rs. {price2}"
subtotal2 = quantity2 * price2
line5 = f"Subtotal: Rs. {subtotal2}"
line6 = f"Discount: Rs. {discount2}"
final2 = subtotal2 - discount2
line7 = f"Final Amount: Rs. {final2}"

print("\n--- f-string Task 1 / Non-Optimized ---")
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)


# TASK 2:
# Create a formatted employee performance report.
# Display name, department, salary, performance score and a formatted
# percentage using f-string formatting.

# ---------------- METHOD 1: OPTIMIZED ----------------
emp_name = "Sara"
dept = "Software"
salary = 95000
score = 87.4567

print("\n--- f-string Task 2 / Optimized ---")
print(
    f"Employee: {emp_name} | Department: {dept} | "
    f"Salary: Rs. {salary:,.2f} | Score: {score:.2f}%"
)

# ---------------- METHOD 2: NON-OPTIMIZED ----------------
emp_name2 = "Sara"
dept2 = "Software"
salary2 = 95000
score2 = 87.4567

employee_text = f"Employee: {emp_name2}"
department_text = f"Department: {dept2}"
salary_text = f"Salary: Rs. {salary2:,.2f}"
score_text = f"Score: {score2:.2f}%"

report = employee_text + " | " + department_text
report = report + " | " + salary_text
report = report + " | " + score_text

print("\n--- f-string Task 2 / Non-Optimized ---")
print(report)


# ================================================================
# TOPIC 8: input() FUNCTION
# ================================================================
# TASK 1:
# Take user's name, age and city using input().
# Convert age to int and print a personalized message.
#
# NOTE: input() is intentionally demonstrated here. If you run this
# file, this section will pause and ask for input.

# ---------------- METHOD 1: OPTIMIZED ----------------
print("\n--- input() Task 1 / Optimized ---")
user_name = input("Enter your name: ").strip()
user_age = int(input("Enter your age: "))
user_city = input("Enter your city: ").strip()

print(f"Hello {user_name}! You are {user_age} years old and live in {user_city}.")

# ---------------- METHOD 2: NON-OPTIMIZED ----------------
print("\n--- input() Task 1 / Non-Optimized ---")
name_input = input("Enter your name again: ")
age_input = input("Enter your age again: ")
city_input = input("Enter your city again: ")

name_cleaned = name_input.strip()
age_converted = int(age_input)
city_cleaned = city_input.strip()

message_part1 = "Hello " + name_cleaned
message_part2 = "You are " + str(age_converted) + " years old"
message_part3 = "and live in " + city_cleaned

print(message_part1 + ". " + message_part2 + " " + message_part3 + ".")


# TASK 2:
# Build an interactive electricity bill calculator.
# Take units consumed from the user.
# Rate:
# 0-100 units: Rs. 12/unit
# 101-300 units: Rs. 15/unit
# Above 300: Rs. 20/unit
# Add a fixed meter charge of Rs. 250.

# ---------------- METHOD 1: OPTIMIZED ----------------
print("\n--- input() Task 2 / Optimized ---")
units = int(input("Enter electricity units: "))

if units <= 100:
    rate = 12
elif units <= 300:
    rate = 15
else:
    rate = 20

energy_bill = units * rate
meter_charge = 250
bill = energy_bill + meter_charge

print(f"Units: {units}")
print(f"Rate: Rs. {rate}/unit")
print(f"Energy cost: Rs. {energy_bill:,.2f}")
print(f"Meter charge: Rs. {meter_charge:,.2f}")
print(f"Total bill: Rs. {bill:,.2f}")

# ---------------- METHOD 2: NON-OPTIMIZED ----------------
print("\n--- input() Task 2 / Non-Optimized ---")
units2 = int(input("Enter electricity units again: "))

if units2 >= 0:
    if units2 <= 100:
        rate2 = 12
    else:
        if units2 <= 300:
            rate2 = 15
        else:
            rate2 = 20

    cost_per_unit = rate2
    energy_cost2 = units2 * cost_per_unit
    fixed_charge2 = 250
    total_bill2 = energy_cost2 + fixed_charge2

    print("Units:", units2)
    print("Rate:", rate2)
    print("Energy cost:", energy_cost2)
    print("Fixed charge:", fixed_charge2)
    print("Total:", total_bill2)
else:
    print("Units cannot be negative.")


# ================================================================
# FINAL INTEGRATED TASK 1
# ================================================================
# TOPICS USED:
# Variables, Data Types, Strings + String Functions, Conditionals,
# Arithmetic Operators, Type Casting, f-strings, input()
#
# TASK:
# Build an interactive student result and scholarship calculator.
#
# Take from the user:
# - Student name
# - Roll number
# - Math marks
# - English marks
# - Computer marks
#
# Requirements:
# - Clean the student's name with strip() and title()
# - Convert roll number and marks from strings to integers
# - Calculate total and percentage
# - Determine grade:
#       >= 90 A+
#       >= 80 A
#       >= 70 B
#       >= 60 C
#       >= 50 D
#       below 50 F
# - Scholarship:
#       percentage >= 90 -> 50%
#       percentage >= 80 -> 30%
#       otherwise -> 0%
# - Display a professional report using f-strings.
#
# ---------------- METHOD 1: OPTIMIZED ----------------
print("\n" + "=" * 65)
print("FINAL INTEGRATED TASK 1 / OPTIMIZED")
print("=" * 65)

student_name = input("Student name: ").strip().title()
roll_number = int(input("Roll number: "))
math_marks = int(input("Math marks: "))
english_marks = int(input("English marks: "))
computer_marks = int(input("Computer marks: "))

total = math_marks + english_marks + computer_marks
percentage = total / 300 * 100

if percentage >= 90:
    grade = "A+"
    scholarship = 50
elif percentage >= 80:
    grade = "A"
    scholarship = 30
elif percentage >= 70:
    grade = "B"
    scholarship = 0
elif percentage >= 60:
    grade = "C"
    scholarship = 0
elif percentage >= 50:
    grade = "D"
    scholarship = 0
else:
    grade = "F"
    scholarship = 0

status = "PASS" if percentage >= 50 else "FAIL"

print(
    f"\nStudent: {student_name}\n"
    f"Roll Number: {roll_number}\n"
    f"Total Marks: {total}/300\n"
    f"Percentage: {percentage:.2f}%\n"
    f"Grade: {grade}\n"
    f"Status: {status}\n"
    f"Scholarship: {scholarship}%"
)

# ---------------- METHOD 2: NON-OPTIMIZED ----------------
print("\n" + "=" * 65)
print("FINAL INTEGRATED TASK 1 / NON-OPTIMIZED")
print("=" * 65)

name_raw = input("Student name: ")
roll_raw = input("Roll number: ")
math_raw = input("Math marks: ")
english_raw = input("English marks: ")
computer_raw = input("Computer marks: ")

name_step1 = name_raw.strip()
name_step2 = name_step1.lower()
name_final = name_step2.title()

roll_value = int(roll_raw)
math_value = int(math_raw)
english_value = int(english_raw)
computer_value = int(computer_raw)

math_total = math_value
english_total = english_value
computer_total = computer_value

marks_total = math_total + english_total
marks_total = marks_total + computer_total

percentage_step1 = float(marks_total)
percentage_step2 = percentage_step1 / 300
percentage_final = percentage_step2 * 100

if percentage_final >= 90:
    grade_final = "A+"
else:
    if percentage_final >= 80:
        grade_final = "A"
    else:
        if percentage_final >= 70:
            grade_final = "B"
        else:
            if percentage_final >= 60:
                grade_final = "C"
            else:
                if percentage_final >= 50:
                    grade_final = "D"
                else:
                    grade_final = "F"

if percentage_final >= 90:
    scholarship_final = 50
else:
    if percentage_final >= 80:
        scholarship_final = 30
    else:
        scholarship_final = 0

if percentage_final >= 50:
    status_final = "PASS"
else:
    status_final = "FAIL"

part1 = f"Student: {name_final}"
part2 = f"Roll Number: {roll_value}"
part3 = f"Total Marks: {marks_total}/300"
part4 = f"Percentage: {percentage_final:.2f}%"
part5 = f"Grade: {grade_final}"
part6 = f"Status: {status_final}"
part7 = f"Scholarship: {scholarship_final}%"

print(part1)
print(part2)
print(part3)
print(part4)
print(part5)
print(part6)
print(part7)


# ================================================================
# FINAL INTEGRATED TASK 2
# ================================================================
# TOPICS USED:
# Variables, Data Types, Strings + String Functions, Conditionals,
# Arithmetic Operators, Type Casting, f-strings, input()
#
# TASK:
# Build an interactive online shopping checkout system.
#
# Take from the user:
# - Customer name
# - Product name
# - Product price
# - Quantity
# - Customer city
# - Coupon code
#
# Rules:
# - Clean customer/product/city using strip()
# - Product name should be displayed with title()
# - Coupon should be converted to uppercase
# - Convert price to float and quantity to int
# - Calculate subtotal
# - Coupon:
#       SAVE10 -> 10% discount
#       SAVE20 -> 20% discount
#       otherwise -> no discount
# - Delivery:
#       Lahore -> 200
#       Islamabad -> 250
#       Karachi -> 300
#       Other city -> 400
# - If subtotal after discount >= 10000, delivery is FREE.
# - Add 5% tax after discount and delivery.
# - Display a complete invoice using f-strings.
#
# ---------------- METHOD 1: OPTIMIZED ----------------
print("\n" + "=" * 65)
print("FINAL INTEGRATED TASK 2 / OPTIMIZED")
print("=" * 65)

customer_name = input("Customer name: ").strip().title()
product_name = input("Product name: ").strip().title()
price = float(input("Product price: "))
quantity = int(input("Quantity: "))
city = input("City: ").strip().title()
coupon = input("Coupon code: ").strip().upper()

subtotal = price * quantity

if coupon == "SAVE10":
    discount_rate = 10
elif coupon == "SAVE20":
    discount_rate = 20
else:
    discount_rate = 0

discount_amount = subtotal * discount_rate / 100
after_discount = subtotal - discount_amount

if after_discount >= 10000:
    delivery = 0
elif city == "Lahore":
    delivery = 200
elif city == "Islamabad":
    delivery = 250
elif city == "Karachi":
    delivery = 300
else:
    delivery = 400

tax = (after_discount + delivery) * 5 / 100
final_total = after_discount + delivery + tax

print(
    f"\n{'=' * 45}\n"
    f"{'ONLINE SHOP INVOICE':^45}\n"
    f"{'=' * 45}\n"
    f"Customer       : {customer_name}\n"
    f"Product        : {product_name}\n"
    f"City           : {city}\n"
    f"Quantity       : {quantity}\n"
    f"Unit Price     : Rs. {price:,.2f}\n"
    f"Subtotal       : Rs. {subtotal:,.2f}\n"
    f"Coupon         : {coupon}\n"
    f"Discount       : Rs. {discount_amount:,.2f}\n"
    f"Delivery       : Rs. {delivery:,.2f}\n"
    f"Tax (5%)       : Rs. {tax:,.2f}\n"
    f"Final Total    : Rs. {final_total:,.2f}\n"
    f"{'=' * 45}"
)

# ---------------- METHOD 2: NON-OPTIMIZED ----------------
print("\n" + "=" * 65)
print("FINAL INTEGRATED TASK 2 / NON-OPTIMIZED")
print("=" * 65)

customer_raw = input("Customer name: ")
product_raw = input("Product name: ")
price_raw = input("Product price: ")
quantity_raw = input("Quantity: ")
city_raw = input("City: ")
coupon_raw = input("Coupon code: ")

customer_clean = customer_raw.strip()
customer_lower = customer_clean.lower()
customer_final = customer_lower.title()

product_clean = product_raw.strip()
product_lower = product_clean.lower()
product_final = product_lower.title()

city_clean = city_raw.strip()
city_lower = city_clean.lower()
city_final = city_lower.title()

coupon_clean = coupon_raw.strip()
coupon_final = coupon_clean.upper()

price_number = float(price_raw)
quantity_number = int(quantity_raw)

single_price = price_number
number_of_items = quantity_number
subtotal2 = single_price * number_of_items

if coupon_final == "SAVE10":
    discount_rate2 = 10
else:
    if coupon_final == "SAVE20":
        discount_rate2 = 20
    else:
        discount_rate2 = 0

discount_base = subtotal2 / 100
discount2 = discount_base * discount_rate2
price_after_discount = subtotal2 - discount2

if price_after_discount >= 10000:
    delivery2 = 0
else:
    if city_final == "Lahore":
        delivery2 = 200
    else:
        if city_final == "Islamabad":
            delivery2 = 250
        else:
            if city_final == "Karachi":
                delivery2 = 300
            else:
                delivery2 = 400

tax_base = price_after_discount + delivery2
tax_base_percent = tax_base / 100
tax2 = tax_base_percent * 5

total_before_rounding = price_after_discount + delivery2
final_total2 = total_before_rounding + tax2

header = f"{'ONLINE SHOP INVOICE':^45}"
line = "=" * 45

print(f"\n{line}\n")
print(f"{header}\n")
print(f"{line}\n")
print(f"Customer       : {customer_final}\n")
print(f"Product        : {product_final}\n")
print(f"City           : {city_final}\n")
print(f"Quantity       : {number_of_items}\n")
print(f"Unit Price     : Rs. {single_price:,.2f}\n")
print(f"Subtotal       : Rs. {subtotal2:,.2f}\n")
print(f"Coupon         : {coupon_final}\n")
print(f"Discount       : Rs. {discount2:,.2f}\n")
print(f"Delivery       : Rs. {delivery2:,.2f}\n")
print(f"Tax (5%)       : Rs. {tax2:,.2f}\n")
print(f"Final Total    : Rs. {final_total2:,.2f}\n")
print(f"{line}")
print("\n" + "=" * 65)
print("END OF PRACTICE FILE")
print("=" * 65)
