from random import *

list1=[randint(1,100) for i in range(20)]

print(list1)

num=int(input('number to delete: '))

while num in list1:
    list1.remove(num)

print(list1)