from random import randint
list1=[ ]


for i in range(5):
    num=randint(1,50)
    list1.append(num)

print(list1)

if 20 in list1:  # if there is 20 in the list it adds 5 to it
    i=list1.index(20)
    list1[i] += 5
else:
    print('20 not in the list') # if there isn't 20 it prints the message that there isn't 20 there
print(list1)

for i in list1:
    if i%3==0:
        print(i)