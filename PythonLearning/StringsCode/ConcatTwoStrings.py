# #Add two String
str1=input("Enter input: ")
str2=input("Enter input: ")
result=str1 + str2
print(result)
#
# #Add space between them
str1=input("Enter input: ")
str2=input("Enter input: ")
result=str1 +" "+ str2
print(result)
#
# #Add new line between them
str1=input("Enter input: ")
str2=input("Enter input: ")
result=str1 +"\n"+ str2
print(result)
#
# #Add using fstring
str1=input("Enter input: ")
str2=input("Enter input: ")
result=f"{str1 } { str2}"
print(result)


#Takes two user inputs
#Concatenates with a space
#Adds punctuation (a period)
#Writes the result to a text file

str1=input("Enter input: ")
str2=input("Enter input: ")
result=str1+" "+str2+"."
print(result)
with open ("python.txt", "w") as file:
    file.write(result)
# Re-open the file in read mode to check the contents
with open("python.txt", "r") as file:
    content = file.read()
    print("File contains:", content)

