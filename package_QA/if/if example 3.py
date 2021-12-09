name=input("enter student name: ")
if name=="": # == when it's a question (is the name idan?), = it's when you define it as the value.
    name="no name"

grade=(input("enter grade: "))
if grade=="":
    grade=0
else:
    grade=int(grade)

if grade>70 and (name=="lenny" or name=="idan"):
    print(name, "passed")

else:
    print(name, "failed")

