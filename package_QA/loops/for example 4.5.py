sum=0
count=0

for i in range(5):
    price=int(input('enter price: '))
    if sum+price>200:
        print("too expensive, i don't want this prouduct" )
        continue
    sum+=price
    count+=1
    if sum>200:
        print('too expensive, spend less you spoiled fuck')
        break
else:
    print('we completed the shopping and were financially stable about it!')

print('sum', sum, 'count',count)
print('average', sum/count)