from unittest import TestCase, mock
from students import students

class Teststudents(TestCase):

    def setUp(self):
        print('setUp')
        self.student1=students(123,'name',101)
        self.student2=students(123,'name',-1)
        self.student3=students(123,'name',71)
        self.student4=students(123,'name',69)

    def tearDown(self):
        print('tearDown')

    def test_check_pass(self):
        self.assertTrue(self.student1.check_pass())
        self.assertFalse(self.student2.check_pass())
        self.assertTrue(self.student3.check_pass())
        self.assertFalse(self.student4.check_pass())

    def test_update_grade(self):
        self.assertGreater(self.s)

    def test_show(self):
        self.fail()
