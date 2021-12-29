# this program gets a number and checks if its a prime number or not
num=int(input('enter number: '))

for i in range(2,num):
     if num%i==0:
         print('not prime')
         break
else:
    print('prime number')
