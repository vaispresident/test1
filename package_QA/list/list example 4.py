from random import *
list1=[]

for i in range(10):
    numbers=[]
    for j in range(2):
        numbers.append(randint(1,100))
    list1.append(numbers)

print(list1)

list2=[]
for item in list1:
    for i in item:
        if i%3==0:
            print(item)
            break

for item in list1:
    if item[0]%3==0 and item[1]%3==0:
        print(item)
            # if item not in list2:
            #     list2.append(item)

