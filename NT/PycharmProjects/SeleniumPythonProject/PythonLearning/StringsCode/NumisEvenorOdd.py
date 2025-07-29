#Check given num is Even or Odd
x=int(input("Enter a number."))
if x % 2 == 0:
    print(f"{x} is Even")
else:
    print(f"{x} is Odd")

#Check given n num is Even or Odd
x=int(input("Enter a number."))
for i in range(1,x+1):
    if i % 2==0:
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")

#Check Even or Odd using for Loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers:")
for num in numbers:
    if num % 2 == 0:  # If the remainder when divided by 2 is 0, it's even
        print(num,end=" ")

print("\nOdd numbers:")
for num in numbers:
    if num % 2 != 0:  # If the remainder when divided by 2 is not 0, it's odd
        print(num, end=" ")

#Check Even or Odd separating 2 lists
x=int(input("\nEnter a number."))
Even=[]
Odd=[]
for i in range(1,x+1):
    if i%2==0:
        Even.append(i)
    else:
        Odd.append(i)
print(f"\nEven Number: {Even}")
print(f"Odd Number: {Odd}")




