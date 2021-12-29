def sum(a):
    return ((a%10)+(a//10%10)+(a//100))
a=int(input('enter number: '))
print(sum(a))
