from random import *
list1=[randint(1,100) for  i in range(20)]

print(list1)

listdiv3=[]

for i in list1:
    if i%3!=0:
        listdiv3.append(i)

list1=listdiv3
print(list1)