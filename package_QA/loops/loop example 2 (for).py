from random import randint,randrange
for i in range(1,6):# goes from 1 till 5
    print(i)
    num = randint(10, 99)
    print('i', i, 'num', num)
    if num % 7 == 0 or num & 10 == 7 or num // 10 == 7:
        print('lucky lucky')
    else:
        print('unlucko maloko')
