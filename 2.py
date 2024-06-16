#Lists ex1

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#Lists ex2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#Lists ex3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#Lists ex4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

#Lists ex5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#Lists ex6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#Lists ex7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#Lists ex8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))


#Tuples ex1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#Tuples ex2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#Tuples ex3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#Tuples ex4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])


#Sets ex1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#Sets ex2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#Sets ex3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#Sets ex4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#Sets ex5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")


#Dictionaries ex1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#Dictionaries ex2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"]= 2020

#Dictionaries ex3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#Dictionaries ex4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#Dictionaries ex5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()


#If... else ex1
a = 50
b = 10
if a > b:
  print("Hello World")

#If... else ex2
a = 50
b = 10
if a != b:
   print("Hello World")

#If... else ex3
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")

#If... else ex4
a = 50
b = 10
if a == b:
  print("1")
elif a >b:
  print("2")
else:  
  print("3")

#If... else ex5
if a == b and c == d:
   print("Hello")

#If... else ex6
if 5 > 2:
  print("YES")

#If... else ex7
a = 2
b = 5
   print("YES") if a == b else  print("NO")

#If... else ex8
a = 2
b = 50
c = 2
if a == c or b == c:
   print("YES")


#While loops ex1
   i = 1
while i < 6:

  print(i)
  i += 1

#While loops ex2
  i = 1
while i < 6:
  if i == 3:
    
   break
 i += 1

#While loops ex3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
print(i)

#While loops ex4
i = 1
while i < 6:
  print(i)
  i += 1
else:
 print("i is no longer less than 6")


 #For loops ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
 print(x)

#For loops ex2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
   print(x)
  
#For loops ex3
for x in range(6):
  print(x)

#For loops ex4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
print(x)

