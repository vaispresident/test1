from random import *
list1=[ ]

for i in range(10):
    num=randint(1,50)
    list1.append(num)

print(list1)


for i in range(len(list1)):
    list1[i]*=2
print(list1)