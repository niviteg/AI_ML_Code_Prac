#Create newlist based on value of an existing values
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[]

for x in fruits:
    if 'e' in x:
        newlist.append(x)
print(newlist)

#Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)      #will convert tuple in to list
y[1] = "kiwi"    #will update index 1 value with new value
x = tuple(y)     #once the new list is updated convert it to Tuple
print(x)         #Tuple value is changed


#Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)     #When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.
thistuple += y
print(thistuple)


#Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#Basic code using if condition check b is greater than q
a = 33
b = 200
if b > a:
  print("b is greater than a")

if a > b: print("a is greater than b")  # Short hand if condition

#Elif
#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

a = 33
b = 33
if b > a:       # if condition is not true it will got to elif
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


#One line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")

#The and keyword is a logical operator, and is used to combine conditional statements:
#Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#The or keyword is a logical operator, and is used to combine conditional statements:
#Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
#Test if a is NOT greater than b:

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#Nested If
#You can have if statements inside if statements, this is called nested if statements.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


#The break Statement
#With the break statement we can stop the loop even if the while condition is true:
#Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
