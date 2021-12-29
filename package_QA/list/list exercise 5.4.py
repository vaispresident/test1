list1=[]
list2=[]
for i in range(5):
    num1=int(input('num1: '))
    list1.append(num1)
    num2=int(input('num2: '))
    list2.append(num2)

print(list1+list2)
print(len(list1+list2))
# list1+=list2
# print(list1)
# print(len(list1))