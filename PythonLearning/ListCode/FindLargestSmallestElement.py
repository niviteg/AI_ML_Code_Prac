#Basic Example
num=[10,30,50,70,20,40,60,80]
largest=max(num)
smallest=min(num)
print(f"Largest Number: {largest} \nSamllest Number:{smallest}")


#With User Input
user_input = input("Enter numbers separated by commas: ")
parts=user_input.split(",")
numbers=[]
for x in parts:
    x=x.strip()
    num=int(x)
    numbers.append(num)
#numbers = [int(x.strip()) for x in user_input.split(",")]

# Find and print
print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))









