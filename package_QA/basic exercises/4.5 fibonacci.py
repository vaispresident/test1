# get a size of a fibonacci number and print the numbers
num=int(input('enter number: '))

number1=0
number2=1

print(number1,end=' ')
print(number2,end=' ')

for i in range(num-2):
    print(number1+number2,end=' ')
    number3=number1+number2
    number1=number2
    number2=number3