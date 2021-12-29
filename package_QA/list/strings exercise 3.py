text=input('enter text: ')
letter=input('enter letter: ')
for i in range(len(text)):
    if letter==text[i]:
        print('letter found in spot:',i+1)
        break
else:
    print('-1')