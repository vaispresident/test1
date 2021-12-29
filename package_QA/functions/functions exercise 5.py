def sum_all(a,b,c,d,e):
    count=0
    for i in range(a,e+1):
        count+=1
    return count

num1=int(input('enter number 1: '))
num2=int(input('enter number 2: '))
num3=int(input('enter number 3: '))
num4=int(input('enter number 4: '))
num5=int(input('enter number 5: '))

print(sum_all(num1,num2,num3,num4,num5))