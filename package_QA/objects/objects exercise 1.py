class cus:
    def __init__(self,course_num,course_name,num_of_students,max_students):
        self.course_num=course_num
        self.course_name=course_name
        self.num_of_students=num_of_students
        self.max_students=max_students

    def __str__(self):
        return f'course number:{self.course_num} ' \
               f'course name:{self.course_name} ' \
               f'number of students in the course:{self.num_of_students} ' \
               f'maximun numbers of students that can be in a course:{self.max_students}'

    def free_space_in_course(self):
        free_space_in_course=self.max_students-self.num_of_students
        return free_space_in_course

    def new_students(self,a):



course1=cus(course_num=' ',course_name=' ',num_of_students=' ',max_students=' ')
print(course1)