grade=int(input('enter grade: '))
sum=0
count=0
sum1=0
count1=0
while 0<=grade<=100:
    if grade>=60:
        sum+=grade
        count+=1
    else:
        sum1+= grade
        count1+= 1
    grade=int(input('enter grade: '))

print('sum passed: ', sum)
print('sum failed: ',sum1)

print('average passed: ',sum/count)
print('average failed: ',sum1/count1)
