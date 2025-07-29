#Remove duplicates using set()
numbers = [1, 2, 2, 3, 4, 4, 5]
duplicate=set(numbers)
duplicate=list(duplicate)
print(duplicate)

#Using for Loop
numbers=[1,2,2,3,4,4,5]
unique_numbers=[]
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(unique_numbers)

#With Dictionary
numbers=[1,2,2,3,4,4,5]
unique_numbers=list(dict.fromkeys(numbers))
print(unique_numbers)



