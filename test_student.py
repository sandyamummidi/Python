#from student import Student
from student import Student
import unittest

class teststudent(unittest.TestCase):
    def test_email(self):
        ob=Student("san","mum",85)
        self.assertEqual(ob.email,"san.mum@gmail.com")

    def test_fullname(self):
        obj1=Student("san","mum",60)
        self.assertEqual(obj1.fullname,"san mum")

    def test_apply_bonus(self):
        obj2=Student("san","mum",90)
        self.assertEqual(obj2.marks,90)
        obj2.apply_bonus()
        self.assertEqual(obj2.marks,135)

    def test_something(self):
        obj3=Student("san","mum",85)
        obj3.something("middlename")
        self.assertEqual(obj3.somevalue,"san.mum@gmail.comsan mummiddlename")


if __name__=="__main__":
    unittest.main()




















#ob.test_email()
#        self.assetEqual(ob.email,"ee dd 90")