class std:
    def __init__(self, name, rollno, age):
        self.name = name
        self.rollno = rollno
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name}")

s1 = std("Ali", 101, 20)
s1.greet()
s1.name = "Ahmed"
s1.greet()

# car class with brand and year attribute and prints description
# two diff car obj with dif val call method oon both
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def print_description(self):
        print(f"This is a {self.year} {self.brand}.")

# Create an instance of the Car class
car1 = Car("Toyota", 2020)
car1.print_description()
car2 = Car("Honda", 2021)
car2.print_description()

class student:
    school = "navttc"
    def __init__(self,name):
        self.name = name

s1=student('ali')
s2=student('sarah')
print(s1.school, s2.school, s1.name)

# create class employee with class var company shared by aoll and instance var name
# create 3 obj empolyee and print their name and confirm all share same company value
class employee:
    company = "NETSOL"
    def __init__(self,name):
            self.name = name

    def print_value(self):
        print(f"My name is {self.name} and company is {self.company}")

e1 = employee("ali")
e2 = employee("ahmed")
e3 = employee("faiz")
e=[]
e.append(e1)
e.append(e2)
e.append(e3)
for i in range(3):
    e[i].print_value()

# constructor and desctrutor : auto call for using auto deletion destructor
class destruction:
    def __init__(self,name):
        self.name = name
        print(f"{self.name} created")
    def before_des(self):
        print(self.name)
    def __del__(self):
        print(f"{self.name} destroyed can't access it now")
    def after_des(self):
        print(self.name)

d1 = destruction("usman")
d1.name = "ahmed"
print(d1.name)
d1.before_des()
d1.after_des()

# create book calass whose constructor prints book added with title and desctructor print book removed
# create a book object then delete it using del and observe both message

class book:
    def __init__(self, title):
        self.title = title
        print(f"{self.title} book created\n")
    def __del__(self):
        print(f"\n{self.title} book removed")

b1 = book("let us c")
# b1.__del__() destructor when one obj try to use multiple class first class things will destroy for that obj

class animal:
    def eat(self):
        print("eating")
class dog(animal):
    def bark(self):
        print("barking")

d = dog()
d.eat()
d.bark()

# create veh clas with start() then car class inherit form it and adds honks
# create hierarchical example one shape parent class with circle and square two sep children
class veh:
    def start(self):
        print("starting the car")
class car(veh):
    def horn(self):
        print("its honking now")

c1 = car()
c1.start()
c1.horn()

class shape:
    def __init__(self):
        self.radius = int(input("enter the radius of the shape : "))

class circle(shape):
    def area(self):
        self.area = self.radius*3.14*self.radius
        print("area of circle",self.area)

class square(shape):
    def area(self):
        self.area = (self.radius*2)**2
        print("area of square",self.area)

c1 = circle()
c1.area()
s1 = square()
s1.area()
c2 = circle()
c2.area()

# multilevel inheritence
class flyer:
    def move(self):
        print("flying...")

class swimmer:
    def move(self):
        print("swimming...")
class duck(flyer,swimmer):
    pass

d = duck()
d.move()
swimmer.move(d)

# two parent class phone and camera with function and smart_phone call both of them
class phone:
    def open(self):
        print("dial num or give call")
class camera:
    def open(self):
        print("open a camera or click photo")
class smart_phone(phone,camera):
    def __init__(self):
        camera.open(self)
        phone.open(self)

s_p_1 = smart_phone()
s_p_1.open() #call the open function of phone
camera.open(s_p_1) #for calling camera for smart_phone_1 obj

# access specifier (default is public) (_pin=1 protected) (__pin=12 private)
class access_specifier:
    def __init__(self,Class):
        __name = "usman" #private name
        self.Class = Class #public class
        _school = "bets" #protected school 
        print("access all three here inside same class",__name," ",self.Class," ",_school)

a_s_1 = access_specifier("navttc")
print(a_s_1.Class)
# print(a_s_1._school) can't access

# class account public bank_holder protected _branch and private __pin 
# try access pin from outside the class see the error.
class account:
    def __init__(self,account_holder):
        __pin = "pakistan123" #private name
        self.holder = account_holder #public class
        _branch = "Lahoreb1" #protected school 
        print("access all three here inside same class",__pin," ",self.holder," ",_branch)

a1 = account("usman")
print(a1.holder)
# print(a1.__pin)  account no attribute __pin error

class cat:
    def speak(self):
        print("meow..")

class dog:
    def speak(self):
        print("bow bow..")

animals = [cat(),dog()]
for animal in animals:
    animal.speak()

# two class circle shape with function area calling both functions through loop.
# point(x,y)  overlord with + operator __add__ so two points can be added togather
class circle:
    def area(self):
        print("area of circle")

class shape:
    def area(self):
        print("area of any shape")

for shape in [circle(),shape()]:
    shape.area()

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y) #self = p1 and other = p2

    def display(self):
        print(f"({self.x}, {self.y})")


p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2 #here + auto calls __add__ function p1.__add__(p2)

p3.display()

class book:
    def __init__(self,title):
        self.title = title
    def __str__(self):
        return f"Book : {self.title}"

b = book("Python lab 1")
print(b)

# without return how to use
class copy:
    def __init__(self,title):
        self.title = title
    def __str__(self):
        print(f"your copy : {self.title}")

b = copy("my copy")
b.__str__()

#create a product class with __init__ and __str__ that neatly display name and price
# add length __len__ method to class that that tell num of items in a list 
class Product:
    def __init__(self, name, price, items):
        self.name = name
        self.price = price
        self.items = items  # a list, e.g. quantity units or components

    def __str__(self):
        return f"Product: {self.name} | Price: ${self.price:.2f}"

    def __len__(self):
        return len(self.items)


# ---- Demo ----
p1 = Product("Laptop", 799.99, ["charger", "manual", "laptop"])
p2 = Product("Mouse", 19.5, ["mouse"])

print(p1)          # calls __str__
print(len(p1))     # __len__ -> 3

print(p2)
print(len(p2))     #__len__ -> 1

# dynamic polymorphism
class circle2:
    def area(self):
        print("area of circle")

class shape2:
    def area(self):
        print("area of any shape")

for shape in [circle2(),shape2()]:
    shape.area()

# base class employee with method pay and manager with same pay method 
# put employee and maanger in list and obser difference
class employee:
    def pay(self):
        emp_pay_base = 1200
        print("employee pay",emp_pay_base)
class manager:
    def pay(self):
        manager_pay_base = 2000
        print("manager pay",manager_pay_base)

for shape in [manager(),employee()]:
    shape.pay()


from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(x=3, y=5)  # keyword args
print(p)  # auto-generated __repr__ that is print("x = {x}, y = {y}")

# Abstract class

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def area(self):
        return 10 * 5


r = Rectangle()
print(r.area())