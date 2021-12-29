sum=0
count=0

for i in range(5):
    price=int(input('enter price: '))
    sum+=price
    count+=1
    if sum>200:
        print('too expensive, spend less you spoiled fuck')
        break

print('sum', sum, 'count',count)
print('average', sum/count)