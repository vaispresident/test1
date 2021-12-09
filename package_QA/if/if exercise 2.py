num1=int(input("random number 1: "))

if 100<=num1<=999:
    print(int(num1%10)+(num1//10%10)+(num1//100))
else:print("error")


