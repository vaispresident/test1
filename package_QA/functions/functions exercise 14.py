from random import *

def list_grades(num):
    list1 = [randint(1,100) for i in range(num)]
    return list1
num=int(input('number of students: '))
print(list_grades(num))

# exercise 15
def avg(*numbers):
    print(numbers)
    return sum(numbers)/(len(numbers))
print(avg(list_grades(num)))