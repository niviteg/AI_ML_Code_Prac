# #Adding 2 numbers
# num1 = 1
# num2 = 9
# sum_results= num1 + num2
# print("The sum of num1 and num2 numbers is : ", sum_results)
#
# #Finding the Maximum of Two Numbers
#
# num1= 10
# num2= 8
#
# if num1 > num2:
#     print(num1,"is greater")
# else:
#     print(num2,"is greater")
#
# # #Check if a num is even or odd
# num= [1,2,3,4,5,6,7,8,9,10]
# squared_num = map(lambda x: x*2,num)
# print(list(squared_num))
#
# even_num=filter(lambda x: x%2 == 0,num)
# print(list(even_num))
#
#
# # #Check even or odd when there is range
# # numbers = range(1, 11)
# #
# # for number in numbers:
# #     if number % 2 == 0:
# #         print(f"{number} is even")
# #     else:
# #         print(f"{number} is odd")
#
# #Calculate Factorial of a Number.
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print("Factorial of 5 is:", factorial(5))
#
# number = [2,7,8,9,5,8]
# map_number= map(lambda x : x *2,number)
# print(list(map_number))
# result_List= list(map_number)
#
# even_num=filter(lambda x:x%2==0,result_List)
# print(even_num)
#
# num = range(1,10)
# even=[]
# odd=[]
#
# for x in num:
#         if x % 2 == 0:
#            print("Even",x)
#         else:
#            print("Odd",x)
#
# even.append(list[x])
# odd.append(list[x])
#
#
#
#
#
#
#
#
#
#
# # even = []
# # odd=[]
# # listmap=list(map_number)
# # print(len(listmap))
# # for i in range(len(listmap)):
# #     if listmap[i]%2==0:
# #         even.append(listmap[i])
# #     else:
# #         odd.append(listmap[i])
# # print(even)
# # print(odd)
#
# # even_num = filter(lambda x : x % 2 == 0,list(map_number))
# # print(list(even_num))
#
#
# #even_numbers = list(filter(lambda num: num % 2 == 0, map_number))
#
# # even = []
# # odd = []
# # for x in range(len(map_number)):
# #     if map_number[x]//2 == 0:
# #         even.append(map_number[x])
# #     else:
# #         odd.append(map_number[x])
#
# #filer_number=filter(lambda x : x % 2 == 0,number)
#
#
#
#
from selenium.webdriver.remote.webelement import isDisplayed_js

# def check_positive_odd_even(number):
#
#   if number <= 0:
#     return "Not a positive number"
#   elif number % 2 == 0:
#     return "Even"
#   else:
#     return "Odd"
#
# # Example usage:
# num1 = 11
# print(f"{num1} is {check_positive_odd_even(num1)}")
#
# num2 = 5
# print(f"{num2} is {check_positive_odd_even(num2)}")
#
# num3 = -1
# print(f"{num3} is {check_positive_odd_even(num3)}")

x=float(1)
y=int(2.5)
z=complex(1j)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))