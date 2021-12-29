a=50
list1=[10,11,12,13,'aa','bb',5.4,35,50]
print('list[2]',list1[2])
a=45 # the value of a doesn't change in the list
list1[3]=30
print(list1)
list1[3]=list1[2]*2
print(list1)
list1[3]+=2
print(list1)

list1.append(100) # adds a value to the end of the list
print(list1)
list1+=[1,2,3,4]
print(list1)
list2=[20,21,22,23]
list1+=list2
print(list1,list2)
print('list2*3',list2*3)
print('len(list2*3)',len(list2*3))
print('len(list1',len(list1))
list1.remove(100)
print(list1)
del list1[0]  # deletes the cell number
