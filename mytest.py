#@Time   : 2019/7/24 13:00
#@Author : jackman


import unittest
from other.myBig import Big

class TestBig(unittest.TestCase):
    def setUp(self):
        self.big = Big(999999999999999999,2)

    def tearDown(self):
        self.big = None

    def testadd(self):
        print('test add')
        self.assertEqual(self.big.add(), '1000000000000000001')

    def testmul(self):
        print('test mul')
        self.assertEqual(self.big.mul(), '1999999999999999998')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestBig("testadd"))
    suite.addTest(TestBig("testmul"))
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest='suite')
