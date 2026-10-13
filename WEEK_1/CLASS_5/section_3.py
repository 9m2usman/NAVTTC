# # # if elif nested condition
# # marks = 75
# # if marks>=90:
# #     print("grade A")
# # elif marks>=70:
# #     print("grade B")
# # else:
# #     print("fail")

# # #task grading : 4 grade a b c and fail
# # marks = 90
# # if(marks>=90):
# #     print("Grade A")
# # elif(marks>=80):
# #     print("Grade B")
# # elif(marks>=70):
# #     print("Grade C")
# # else :
# #     print("fail")

# # #task2 nested coditon : only allow to ean event if age>=18 and has tiket it true
# # age = int(input("enter age : "))
# # has_ticket=True
# # if(age >=18):
# #     if(has_ticket):
# #         print("allow entry")
# # else:
# #     print("not allowed entry")

# # age2 = int(input("enter age second time : "))
# # has_ticket2 = True
# # if(age2 >= 18 and has_ticket2):
# #     print("allow")
# # else:
# #     print("not allow")

# # ternary operator
# age = 20
# status = "adult" if age >= 18 else "minor"
# print(status)

# # write a ternary op print pass or fail based on marks ba pass_marks=40
# marks = int(input("enter marks"))
# is_pass = "pass" if marks >= 40 else "fail"
# print(is_pass);

# print("pass" if marks>=50 else "fail")

for i in range(10,1,-1):
    if i == 5:
        break
    print(i)
for i in range(6):
    if i%2 == 0:
        continue
    print(i)

# print num from 1 to 20 but stop completely when u reach 15(use break)
for i in range(20):
    if i ==15:
        break
    print(i)

# print num form 1 to 20 but skip any num that is multiple of 3
for i in range(20):
    if i % 3 == 0:
        continue
    print(i)

# enumerates : it gives both index and value of list
fruits = ["apple","banana","mango"]
for index,fruit in enumerate(fruits):
    print(f"index = {index} fruit = {fruit}")

# list of 5 fav food and loop thru and printing each with its pos using enumearate
foods = ["pizza","burger","biryani","pasta","sushi"]
for index,food in enumerate(foods):
    print(f"{index} : {food}")

# use for loop with range() to orint first 10 square numbers (1,4,9....)
for i in range(1,11):
    print(f"square of {i} = {i*i}")
    # or print(i**2)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# while loop that pritns all even num from 2 to 20
num = 2
while num <= 20:
    print(num)
    num += 2

# countdown from 10 to 1 using while loop while print "liftoff"
num = 10
while num >= 1:
    print(num, ": liftoff")
    num -= 1

# nested loops
for i in range(1, 5):
    for j in range(1, 11):
        print(f"{i} * {j} = {i*j}")
    print("  --------\n  --------")

# print full 5 x 5 multiplication table using nested loops
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} * {j} = {i*j}")
    print("  --------\n  --------")

# use nested loop stars logic
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()