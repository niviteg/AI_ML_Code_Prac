#1
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
         if char in vowels:
             count +=1
    return count

S=input("Enter word: ")
print("number of vowels",count_vowels(S))

#2
count = lambda s: sum(1 for c in s if c.lower() in "aeiou")

text = input("Enter a word: ")
print("Number of vowels:", count(text))
