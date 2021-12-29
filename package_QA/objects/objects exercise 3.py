class person:
    def __init__(self,name,age,num_of_kids):
        self.name=name
        self.age=age
        self.num_of_kids=num_of_kids

    def age_group(self):
        if 0<=self.age<=18:
            return 'child'
        elif 19<=self.age<=60:
            return 'adult'
        elif 61<=self.age<=120:
            return 'senior'

    def __str__(self):
        return f'{self.name}\n' f'age:{self.age}\n'f'number of kids:{self.num_of_kids}'

    def has_kids(self):
        if self.num_of_kids>=1:
            return True
        else:
            return False


name=input('enter name: ')
age=int(input('enter age: '))
num_of_kids=int(input('enter number of kids: '))
person1=person(name,age,num_of_kids)
print(person1) # __str__ here
if person1.has_kids():
    print(f'{name} has kids')
else:
    print(f"{name} doesn't have kids")
print(person1.age_group())

