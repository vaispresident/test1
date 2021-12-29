from random import *

def init_list_random(list1:list):
    for i in range(20):
        list1.append(randint(1,100))
        # list1[:]=[randint(1,100) for i in range(20)]

def num_count_list(num:int, list1:list):
    return list1.count(num)

def location_max_num(numbers:list): # exercise 13
    return numbers.index(max(numbers))

list1=[]
init_list_random(list1)
print(list1)
num=int(input('number: '))
print(f' {num} found {num_count_list(num,list1)} times')
print(f'max number in location {location_max_num(list1)}')