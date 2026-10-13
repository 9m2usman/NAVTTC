def add_num(a,b):
    result = a+b
    return result

sum_num = add_num(5,3)

def mul_num(a,b):
    return a*b

mul_num = mul_num(int(input("enter first num : ")),int(input("enter sec num : ")))
print(mul_num)

def div_num(a,b):
    if(b==0):
        print("dividend can't be zero")
    else:
        print(a/b)

div_num(20,4)

# write func called sqaure n return the square of num call it with 3 different numberrs.

def square_num(n):
    return int(n**2)

print(square_num(5))
print(square_num(51))
print(square_num(7))

def square_nums(a,b,c):
    print(int(a**2),int(b**2),int(c**2))

square_nums(4,5,6)
# write fun greet(name) that return personalized grettin strin like hello, ali
def greeting(name):
    print("hello",name)

greeting("usman")

# # local vs gloabal function
x = 10
def my_func():
    y = 5
    print("sum of local and global function is : ",x+y)

my_func()
# print(x) true its a global var
# print(y) false cant do this its a local var 


# global var and func with own local var print both from inside the func

a=5
def func():
    b=6
    print(a,b)
func()
# try printing the local var from outside and observe error its produce
# print(b) error b is not defined

# lambda func used for returning and simple single line func

square = lambda x: x*x
print(square(5))

add = lambda a,b: a+b
print(add(5,7))

check = lambda x: "adult" if(x>18) else "not adult"
print(check(10))

# lambda mul two num and test for two diff pair of nums
mul = lambda a,b: a*b
print(mul(5,6),"\n",mul(4,5))

# lambda check whether num is even reurning true or false
is_even_or_odd = lambda x: "true" if x%2==0 else "false"
print(is_even_or_odd(7))
 
# map and filter map(lambda var, expression, list_var or dict_var)
nums = [1,2,3,4,5]
squared = list(map(lambda x: x*x, nums))
print(squared)

evens = list(filter(lambda x: x%2==0,nums))
print(evens)

# use map with lambda to convert a list of celsius temp to fahrenhiet
list_celsuis = [2,4,6,7,8,7]
celsuis_to_fahrenhiet = list(map(lambda x: x*1.8+32,list_celsuis))
print(celsuis_to_fahrenhiet)

# use filter with lambda to keep only num greater than 10 from a list of your choice
numbers = [20,10,4,30,25,3]
num_grt_ten =  list(filter(lambda x: x>10, numbers))
print(num_grt_ten)

# # inner and outer functions
def outer(outer_text,inner_text):
    def inner(inner_text):
        print("hi i am accesing inner var plus outer var")
        print(outer_text,inner_text)
    inner(inner_text)

outer("hello","usman")

# outer fun proces_ord item with inner func print formatted receopt line
items = {
    "laptop":{
        "vers":12,
        "price":1200,
        "quantity":3
    },
    "phone":{
        "vers":10,
        "price":1100,
        "quantity":6
    }
}
def proc_ord(item):
    def print_item():
        print("receipt item : ")
        for item in items.items():
            print(f"item = {item[0]} \nversion = {item[1]['vers']} \nprice = {item[1]['price']} \nquantity = {item[1]['quantity']}\n")
    print_item()
proc_ord(items)

# modify it so the inner func also cal and prit 10% disc on a given price
def prod_ordr(item):
    def inner_ordr():
        for i in item.items():
            price = i[1]['price']
            discount_price = price - 0.1*price
            print(f"10% discounted price of item {i[0]}: {discount_price}")
    inner_ordr()

prod_ordr(items)

# read and write 
# create new file write it append it and then write again and see the difference
with open("file.txt", "w") as f:
    f.write("hello world")

with open("file.txt","w") as f:
    f.write("welcome back")

with open("file.txt","a") as f:
    f.write("\nwhat are you gonna write now.")

with open("file.txt","r") as f:
    content = f.read()
    print(content)

with open("scores.txt","w") as f:
    f.write(f"first_subject_score = {int(input('enter first subject score : '))}\nsecond_subject_score = {int(input('enter second subject score : '))}\n")

with open("scores.txt","a") as f:
    f.write(f"third_subject_score = {int(input('enter third subject score : '))}\n")

with open("scores.txt","r") as f:
    content = f.read()
    print(content)

# exception handling
try:
    num = int(input("enter ur num : "))
    print(int(10/num))
except ZeroDivisionError:
    print("can't divide by zero")
except ValueError:
    print("this is not a num")
finally:
    print("done try")

# try/except block that safely dividies two user input num handling division by zero
# add second except block that cathches invalid non numeric input and prints a friendly message
try:
    num1=int(input("enter your first num : "))
    num2=int(input("enter your second num: "))
    print(num1/num2)
except ZeroDivisionError:
    print("divisor can't be zero")
except ValueError:
    print("Please enter valid integers")
finally:
    print("division exception handled perfectly")

try:
    num1 = int(input("Enter your first num: "))
except ValueError:
    print("First number must be an integer")
    num1 = None

try:
    num2 = int(input("Enter your second num: "))
except ValueError:
    print("Second number must be an integer")
    num2 = None

if num1 is not None and num2 is not None:
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print("Divisor can't be zero")