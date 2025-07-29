#Using Set
List1=[1,2,3,4,5]
List2=[2,5,8,9,1]
comman=list(set(List1)  & set(List2))
print(comman)

#Using for Loop
List1=[1,2,3,4,5]
List2=[2,5,8,9,1]
comman=[]
for i in List1:
    if i in List2 not in comman:
        comman.append(i)
print(comman)

#Using Split
List1=input("Enter List1: ")
List2=input("Enter List2: ")
part1=List1.split(",")
part2=List2.split(",")
number1=[]
number2=[]
for x in part1:
    x=x.strip()
    number1.append(str(x))

for x in part2:
    x=x.strip()
    number2.append(str(x))

comman=list(set(number1) & set(number2))
print("Result:",comman)

sort_num=dict(sorted(comman.items(),key=lambda x:x[1],reverse=True))
print(sort_num)







