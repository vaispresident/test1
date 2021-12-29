from random import *

list1=[randint(1,100) for  i in range(20)]

print(list1)
listdup=[]

for i in list1:
    if i not in listdup:
        listdup.append(i)

print(listdup)