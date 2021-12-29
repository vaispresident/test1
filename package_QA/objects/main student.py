# from package_QA.objects import students
#
# st1=students(21,'idan',79)
# if st1.check_pass():
#     print('passed')
# else:
#     print('failed')
#
# factor=int(input('enter factor: '))
# st1.update_grade(factor)
#
# st1.show
# print(st1)
from package_QA.objects.students import *

st1=students(21,'idan',79)
if st1.check_pass():
    print('passed')
else:
    print('failed')

factor=int(input('enter factor: '))
st1.update_grade(factor)

print(st1)