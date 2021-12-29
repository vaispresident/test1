sum=0
count=0

for i in range(6):
    num = int(input('num: '))
    if num%2!=0:
        print('לא זוגי, ממשיך הלאה')
        continue
    sum+=num
    count+=1
print(sum)
print(sum/count)

