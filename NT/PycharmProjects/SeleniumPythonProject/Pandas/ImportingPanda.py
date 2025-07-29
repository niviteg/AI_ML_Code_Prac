import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

#Create a simple Pandas Series from a list

a=[1,4,8,9]
myvar=pd.Series(a)
print(myvar)

a=['apple','banana','dog','kiwi']
myvar=pd.Series(a)
print(myvar)
print(myvar[3])

#Create your own labels: using index argument
a=[1,2,3,4,5]
myvar=pd.Series(a,index=('a','b','c','d','e'))
print(myvar)

#When you have created labels, you can access an item by referring to the label.
a=[1,2,3,4,5]
myvar=pd.Series(a,index=('a','b','c','d','e'))
print(myvar['a'])



