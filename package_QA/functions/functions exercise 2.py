def num_is_3(a):
    if 100<=a<=999:
        return True
    else:
        return False

num=int(input('enter number: '))

if num_is_3(num):
    print("it's 3 digits")
else:
    print("it's not 3 digits")
