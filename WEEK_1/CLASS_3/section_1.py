# variables and datatypes.......
name = "Ali"
age = 20
height = 5.9
is_std = True

print("name = ",name,"age = ",age,"height = ",height,"is_student = ",is_std)
print(type(name),type(age),type(height))

#task for datatype and variable...create var for ur name age and fac_subj and print each one.
#use type for all three and make surepython guess all three correct
name = "Ali"
age = 20
fav_subj = "Computer Science"
print(name,age,fav_subj)
print(type(name),type(age),type(fav_subj))

#operators + - * / // % < <= > >= ! != and or
a = 10
b = 4
print("a + b = ",a+b,"\na - b = ",a-b,"\na * b = ",a*b,"\na / b = ",a/b,"\na // b = ",a//b,"\na % b = ",a%b);
print(a>b,"\n",a<b,"\n",a==b,"\n",a!=b,"\n",a>=b,"\n",a<=b)
if(a<b or a==b):
    print("one of the condition is true")
elif (a>b and b!=0):
    print("a is greater than b")

#task
#given task = 15 and b=4 print the floor division and remainder of a divided by b.
#check and print is a greater than b and is b greataer than 0
a = 15
b = 2
print("Floor division of a and b = ",a//b,"\nRemainder of a and b = ",a%b)
print("is a greater than b = ",a>b,"\nis b greater than 0 = ",b>0)

#string and string operations
course = "Machine Learning"
print(course[0],course[1],course[2],course[3],course[4])
print(course.upper(),"\n",course.lower(),"\n",course.replace("Machine","Deep"),"\n",course.find("Learning"),"\n",course.split(" "),"\n",len(course) )
print(course[0:6])
print(course[0:7:2])
print("learn in course")

std, score = "Ali",85;
print(f"Student: {std}, Score: {score}")

#task
#take string "deeep learning" --- print it in lowercase and print its total length
#check if the word "deep" exists inside it, then use an f-string to p: the topic is deep learning

learning = "Deep Learning"
print(learning.lower());
print(len(learning));
print(learning.find("Deep"))
print(f"the topic is {learning}")

#input type casting
age = input("enter your age : ");
print(type(age))
age = int(age);
print(age+5);
print(type(age))
height = float(input("enter ur height: "));
print(f"{type(height)} \nheight = {height}")

firstName = input("enter first name : ")
lastName = input("enter last name : ")
fullName = firstName +" "+ lastName
print(f"your full name is {fullName}");

# task
# take two numbers fromt he user using input(), convert them to float, pirnt their product.
# take the users name and birth year, clculate and print heir approxmiate age.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
product = num1 * num2;
print(f"multiplication result of {num1} and  {num2} = {product}")

name = input("enter your name: ")
birthYear = int(input("enter your birth year: "))
currentYear = 2026;
age = currentYear - birthYear;
print(f"{name} age in this year is approximately {age}")
