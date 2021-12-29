class students:
    def __init__(self,id,name,grade):
        self.id=id
        self.name=name
        self.grade=grade

    def check_pass(self):
        if self.grade>=70:
            return True
        else:
            return False
    def update_grade(self,factor):
        self.grade+=factor*self.grade/100
        if self.grade>100:
            self.grade=100
    def show(self):
        print(f"{self.name} id:{self.id} grade:{self.grade}")

    def __str__(self):
        return f'name:{self.name}\n' \
               f'id:{self.id}\n' \
               f'grade:{self.grade}'
