num=int(input('enter number: '))

while 10<=num<=99:
    if num%7==0 or num&10==7 or num//10==7:
        print('lucky lucky')
    else:
        print('unlucko maloko')
    num = int(input('enter number: '))



print("invalid number, QUE OTA???")
