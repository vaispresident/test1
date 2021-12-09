grade=int(input("rntar grade"))

if grade>0 and grade<=100:
    print("valid grade")
else:print("invalid grade")

if grade<0 or grade>100: # a number cant be less than 0 and above 100 at the same time that's why use or
    print("invalid grade")
else:
    print("valid grade")\

if 0<grade<=100:
    print("valid grade")