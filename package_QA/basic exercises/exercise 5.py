num1=str(input("num1: "))
num2=str(input("num2: "))
num3=str(input("num3: "))

num_str=num1+num2+num3  # convert the inputs numbers to string
num=int(num_str)        # converts the string back to integer so we can do math on it
print(num,num*2)
print(f'{num},{num*2}')
print(str(num)+","+str(num*2))