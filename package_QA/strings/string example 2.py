value = input('enter value: ')

#print(value.index('abc'))
# print(value.find('abc'))
# print(value.count('abc'))
if value.isnumeric():
    value=int(value)
    print('true number')
else:
    print('invalid number')

value = input('enter value: ')
print(value.isupper())