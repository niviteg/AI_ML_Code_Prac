#Write a Python code to check if a number is even or odd

# num=int(input("Enter Number:"))
# if (num % 2 )== 0:
#          print(f"{num} is Even")
# else:
#          print("Odd")

def even_odd():
   num = range(1, 10)
   for nums in num:
     if nums % 2 == 0 :
       print(f"{nums} is Even:")
     else:
       print(f"{nums} is Odd:")
#
# [print(x) for x in range (1, 20) if x % 2== 0]
# [print(x) for x in range (1, 20) if x % 2>0]

#Write program to print n number of Even and Odd
n=int(input("enter num"))
for i in range(1,n+1):
    if i%2==0:
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")