import math

def is_prime(num):

    if num<=1:
      return False

    for i in range(2,int(math.sqrt(num))+1):
      if (num % i) == 0:
            return False
    return True


num = int(input("Enter a Number"))
if is_prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")



#2nd way
num1=int(input("Enter a number"))

if num1 > 1:
    for i in range(2, num1):
        if (num1 % i) == 0:
            print(f"{num1} is not a prime number")
            break
    else:
        print(f"{num1} is a prime number")
else:
    print(f"{num1}is not a prime number")



