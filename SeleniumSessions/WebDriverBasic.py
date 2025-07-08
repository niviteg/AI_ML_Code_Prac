from selenium import webdriver
from selenium.webdriver.common.by import By

# driver= webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.get("http://www.google.com")
#
# driver.find_element(By.NAME, "q").send_keys("Naveen Automation Labs")
# print(driver.title)
#
#
# text="Nivedita"
# sorted_text="".join(sorted(text))
# print(sorted_text)

#Sorted()
# numbers=[5, 1 , 9 , 1 , 2 , 8 , 4 , 9]
# sorted_numbers=sorted(numbers)
# print(sorted_numbers)
# print(numbers)

#list_sort
# numbers=[1, 2 ,8, 9, 1,4, 3,0]
# numbers.sort(reverse=True)
# print(numbers)

# words=["apple", "banana", "kiwi", "orange", "carrot", "hsjassdiueuhfjdcjdhhuduefh", "Tomato"]
# sorted_words=sorted(words, key=len)
# print(sorted_words)

# tuples = [(1, 'b'), (2, 'a'), (3, 'c')]
# sorted_tuples = sorted(tuples, key=lambda item: item[1])
# print(sorted_tuples)  # Output: [(2, 'a'), (1, 'b'), (3, 'c')]

#
# people = [
#         {"name": "Alice", "age": 30},
#         {"name": "Bob", "age": 25},
#         {"name": "Charlie", "age": 35}
#     ]
#
# sorted_people=sorted(people,key=lambda person: person["name"])
# print(sorted_people)

#List in Python

# List = [1 , 2 , 'Python' , 3 , 4 , 3 , 5]
# print(List[0])
# print(List[-1])
#
# #Modify element
# List[1] = 'Updated'
# print(List)
#
# List.append(7)
# print(List)
#
# List.remove('Python')
# print(List)
#
# print(List[2:6])
#
# print(List[1:3:2])

#List Slicing

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#slice1 = my_list[2:7]  # Elements from index 2 up to (but not including) index 7
#print(slice1)

# print(my_list[:5])
# print(my_list[5:])
#
# print(my_list[1:9:2])
# print(my_list[1:4:2])
#
# print(my_list[2:4:2])
# print(my_list[1:5:2])

#print(my_list[2:9:2])

# print(my_list[:5])
# print(my_list[5:])
#
# print(my_list[-3:])
# print(my_list[:-3])

print(my_list[::-1])












