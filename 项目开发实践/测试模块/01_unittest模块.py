import unittest
from mytest import test

class PythonProjectsTest(unittest.TestCase):
    def test_to_assertTrue(self):
        # 断言真假
        self.assertTrue(test.get01())



list_nums = [7,9,5]
list_chars = ['m', 'd', 'z', 'l']

class TestPPMath(unittest.TestCase):
    def test_first(self):
        # 比较两个值是否一至
        self.assertEqual(test.last(list_nums), 9)



#
# def main():
#     pytest = TestPPMath()
#     pytest.test_first()
#
#

if __name__ == '__main__':
    unittest.main()

