#lists : changea ble, duplicate allow[1,2,1,1] this is true.., like array,ordered
#list functions: access by index, append(add at last), add, remove, insert(user desire position), pop(1) delete user define position,extend adding multiple at end
fruits = ["apple","mango","banana","banana","banana"]
fruits.append("orange")
fruits.remove("banana")
fruits.insert(1,"blueberry")
print(fruits)
fruits.pop(3)
print(fruits);

#task list of 5 cities and then add another one. print 2nd city the last city and total number of cities.
cities = ['atd','lhr','isb','kar','multan']
cities.append('queta')
cities.remove('lhr')
print(f"{cities[1],cities[-1],len(cities)}")

#tuples: unchangeable, allow duplicate me = (1,1,2,3,1), cant do now me=(1,1,2,3,1,1) or me=(2,1,1,1,3)
color = (224,223,112)
#color2=(int(input()),int(input()),int(input()));
print(f"color1 = {color[0]}\ncolor2 = {color[1]}\ncolor3={color[2]}\ntotal_length = {len(color)}")
#print(color2)

#disctionary: key value pair,.....key must be unique, changeable, key to access value{"name":"usman"}
std = {
    "name":"usman",
     "age":24
}
print(std["name"]);
std["age"]=22
std["city"]="lhr"
for k,v in std.items():
    print(f"key = {k}\n value = {v}")

#task dictionary 4 book with keys: title,author,year....print all key, all val update year to ciurent 1...update
book = {
    "title":"let us c",
    "author":"someone",
    "year":2020
}
for k,v in book.items():
    print(k,"=>",v)

book["year"] = 2026;
print(list(book.keys())[2], "===>", book["year"])

#set: unordered, no duplicate, {1,1,1,2,3,3} ouput={1,2,3}, update adding multiple
nums={1,2,3,3,3}
print(nums);
nums.add(4);
nums.remove(1);
print(3 in nums, nums);

#task take list then convert it into set and then print set....remove one item and show set
numList = [1,2,3,3,4,4,5]
numSet = set(numList)
print(numList,"\n",numSet)
numSet.remove(4)
print(numSet)


# type   syntax   ordered    changeable   duplicate    stores
#    list   []        yes        yes          yes        values
#    tuple  ()        yes      no unchange    yes        values
#    set    {}        no          yes         no         unique values
#    dict {key:value} yes         yes         key no     key:value pair

# dict can access through dict.items() {"mame":1,"user",2} here name:1 and user:2 are items
# and name:1 items[0] = name and user and items[1]=1 and 2 dict.keys and dict.values