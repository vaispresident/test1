list1=[10,11,12,13,"aa","bb",100,5.4,35,100,35]
print("list1.count(100)",list1.count(100))
print(list1)
print("list1.index(35)",list1.index(35))
i=list1.index(35)
list1[i]*=2
print(list1)