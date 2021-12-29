grade=int(input('enter grade: '))
sum=0
count=0

while 0<=grade<=100:
    if grade>=60:
        sum+=grade
        count+=1

    grade=int(input('enter grade: '))





print(sum/count)