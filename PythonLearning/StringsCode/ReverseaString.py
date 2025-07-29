#Write a Python program to Reverse a String?
x="Hello"
y=x[::-1]
print(y)

#Uisng reversed() and join()
n="world"
s="".join(reversed(n))
print(s)

#Using for loop
x="python"
y=""
for char in x:
    y=char+y
    print(y)

#using while loop
n="python"
y=""
index=len(n)-1
while index >=0:
    y=y+n[index]
    index=index-1
    print(y)



