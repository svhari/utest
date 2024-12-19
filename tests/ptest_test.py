# ptest_test.py
# 16 Dec 2024

import unittest

def sum(a,b):
    return a+b

class Test():
    pass
class Test1():
    pass

class SumTest(unittest.TestCase):

    def setUp(self):
        
        print("setUp called")

        self.a = 10
        self.b = 20
    
    def tearDown(self):
        print("tearDown called")

        self.a = 0
        self.b = 0

    def test_sumfunc1(self):

        print("Test-1 called")

        # Act

        result = sum(self.a,self.b)
        # Assert
        self.assertEqual(result, self.a+self.b)

    def test_sumfunc2(self):

        print("Test-2 called")
        # Act

        result = sum(self.b,self.a)
        # Assert
        self.assertEqual(result, self.b+self.a)

    def test_assert(self):
        t1 = Test()
        t2 = t1
        self.assertIs(t1,t2)
    
        

class TestMathOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(2 - 1, 1)




if __name__ == "__main__":
    unittest.main()