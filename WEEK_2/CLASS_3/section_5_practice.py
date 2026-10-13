# Command / Task

# Create an OOP-based Employee Management System.

# Create an abstract Employee class with an abstract work() method.
# Create a Developer class that inherits from Employee.
# Create a SeniorDeveloper class that inherits from Developer to demonstrate multilevel inheritance.
# Create a TeamLead class that inherits from both SeniorDeveloper and Manager to demonstrate multiple inheritance.
# Use __init__, __del__, and __str__.
# Demonstrate public, protected, and private attributes.
# Demonstrate polymorphism by having different employee types implement work() differently.

from abc import ABC, abstractmethod


# =========================================================
# 1. ABSTRACT CLASS
# =========================================================

class Employee(ABC):

    def __init__(self, name, salary):
        self.name = name              # PUBLIC
        self._salary = salary         # PROTECTED
        self.__employee_id = 101      # PRIVATE

        print(f"{self.name} object created")

    @abstractmethod
    def work(self):
        pass

    # Method to access private data
    def get_employee_id(self):
        return self.__employee_id

    # DUNDER METHOD
    def __str__(self):
        return f"Name: {self.name}, Salary: {self._salary}"

    # DESTRUCTOR
    def __del__(self):
        print(f"{self.name} object destroyed")


# =========================================================
# 2. SINGLE INHERITANCE
# Employee → Developer
# =========================================================

class Developer(Employee):

    def work(self):
        print(f"{self.name} is writing code")


# =========================================================
# 3. MULTILEVEL INHERITANCE
#
# Employee
#    ↓
# Developer
#    ↓
# SeniorDeveloper
# =========================================================

class SeniorDeveloper(Developer):

    def review_code(self):
        print(f"{self.name} is reviewing code")


# =========================================================
# 4. ANOTHER CLASS
# Used later for multiple inheritance
# =========================================================

class Manager(Employee):

    def manage_team(self):
        print(f"{self.name} is managing the team")


# =========================================================
# 5. MULTIPLE INHERITANCE
#
# SeniorDeveloper ──┐
#                   ├── TeamLead
# Manager ──────────┘
#
# TeamLead has TWO parents
# =========================================================

class TeamLead(SeniorDeveloper, Manager):

    def lead_project(self):
        print(f"{self.name} is leading the project")


# =========================================================
# 6. ANOTHER EMPLOYEE TYPE
# For POLYMORPHISM
# =========================================================

class Designer(Employee):

    def work(self):
        print(f"{self.name} is designing the UI")


# =========================================================
# 7. CREATE OBJECTS
# =========================================================

developer = Developer("Usman", 70000)

senior = SeniorDeveloper("Ali", 90000)

designer = Designer("Ahmed", 65000)

team_lead = TeamLead("Hamza", 120000)


# =========================================================
# 8. PUBLIC MEMBER
# =========================================================

print("\n--- PUBLIC MEMBER ---")

print(developer.name)

developer.name = "Usman Sarfraz"

print(developer.name)


# =========================================================
# 9. PROTECTED MEMBER
# =========================================================

print("\n--- PROTECTED MEMBER ---")

print(developer._salary)


# =========================================================
# 10. PRIVATE MEMBER
# =========================================================

print("\n--- PRIVATE MEMBER ---")

print(developer.get_employee_id())

# This is not the normal way to access private data:
# print(developer.__employee_id)


# =========================================================
# 11. POLYMORPHISM
# =========================================================

print("\n--- POLYMORPHISM ---")

developer.work()

designer.work()

team_lead.work()


# =========================================================
# 12. MULTILEVEL INHERITANCE
# =========================================================

print("\n--- MULTILEVEL INHERITANCE ---")

senior.review_code()

team_lead.review_code()


# =========================================================
# 13. MULTIPLE INHERITANCE
# =========================================================

print("\n--- MULTIPLE INHERITANCE ---")

team_lead.manage_team()

team_lead.review_code()

team_lead.lead_project()


# =========================================================
# 14. DUNDER METHOD
# =========================================================

print("\n--- DUNDER METHOD ---")

print(developer)


# =========================================================
# 15. PROGRAM END
# =========================================================

print("\nProgram finished")