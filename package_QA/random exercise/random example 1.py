from random import randint,randrange
#
# num=randint(10,99)
# num=randrange(10,20)
#
# print(num)
# import random
# num=random.randint(1,99)
i=1
while i<=5:
    num=randint(10,99)
    print('i',i,'num',num)
    if num % 7 == 0 or num & 10 == 7 or num // 10 == 7:
        print('lucky lucky')
    else:
        print('unlucko maloko')
        i+=1

