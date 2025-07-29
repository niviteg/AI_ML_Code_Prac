#1
import string

x=input("Enter a word: ")
y=x[::-1]
if x==y:
    print("It's a palindrome!")
else:
    print("It's not a palindrome!")

#2
x=input("Enter a sentence: ")
cleaned= ''.join(c.lower() for c in x if c.isalnum())

if cleaned == cleaned[::-1]:
     print("is plaindrome")
else:
    print("is not a palindrome")

