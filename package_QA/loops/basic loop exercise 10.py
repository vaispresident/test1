num=1
count=0
while num!=0:
    num=int(input('enter: '))
    if num%7==0 or num%3==0:
        count+=1
print(int(count-1))
