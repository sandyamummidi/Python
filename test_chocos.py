import unittest
from chocos import Chocolate
class testchocos(unittest.TestCase):

    def testfivestar(self):
        obj = Chocolate("5star","choco",10)
        #obj.fivestar()
        self.assertEqual(obj.fivestar(),"5starchoco",10)


    def test_dairymilk(self):
        san = Chocolate("DairyMilk" ,"DarkChoco and Nuts" ,150)
        san.dairymilk()
        self.assertEqual(san.name,"DairyMilk")

if __name__=="__main__":
    unittest.main(more)
