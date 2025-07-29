#Using collection.Counter
from collections import Counter, defaultdict

my_list=['apple','banana','apple','orange','banana','apple']
frequency=Counter(my_list)
print(frequency)

#Using Dictionary
my_list=[1,2,2,3,5,8,8]
frequency={}
for i in my_list:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)


#Using Defalut Dictionary
my_list=['apple','banana','apple','orange','banana','apple']
frequency=defaultdict(int)
for i in my_list:
        frequency[i]+=1
print(dict(frequency))

#Sorted Frequency
sort_freq=dict(sorted(frequency.items(),key=lambda x:x[1],reverse=True))
print(sort_freq)