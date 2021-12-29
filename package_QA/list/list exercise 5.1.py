list1=[ ]
num=int(input('enter: '))
for i in range(num):
    i=int(input('enter list num: '))
    list1.append(i)
print("max(list1)",max(list1))
print("min(list1)",min(list1))
print("avg(list1)",sum(list1)/num)
