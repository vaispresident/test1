age=int(input("age: "))

while age>120 or age<0:
    print("age invalid")
    age = int(input("number: "))
if 0<=age<18:
    print("child")
if  18<=age<60:
    print("adult")
if 60<=age<=120:
    print("senior")

