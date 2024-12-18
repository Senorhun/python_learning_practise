import unittest
from basic_math_lib import add, subtract, multiply, divide

class TestBasicMathLib(unittest.TestCase):

    def test_math_add_correct(self):
        answer = add(5,10)
        expected = 15
        self.assertEqual(answer, expected)

    def test_math_add_wrong(self):
        answer = add(5,10)
        expected = 0
        self.assertNotEqual(answer, expected)

    def test_math_subtract_correct(self):
        answer = subtract(5,10)
        expected = -5
        self.assertEqual(answer, expected)

    def test_math_subtract_wrong(self):
        answer = subtract(5,10)
        expected = 0
        self.assertNotEqual(answer, expected)

    def test_math_multiply_correct(self):
        answer = multiply(5,10)
        expected = 50
        self.assertEqual(answer, expected)

    def test_math_multiply_wrong(self):
        answer = multiply(5,10)
        expected = 0
        self.assertNotEqual(answer, expected)

    def test_math_divide_correct(self):
        answer = divide(5,10)
        expected = 0.5
        self.assertEqual(answer, expected)

    def test_math_divide_wrong(self):
        answer = divide(5,10)
        expected = 0
        self.assertNotEqual(answer, expected)

    def test_math_divide_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)
    
if __name__ == '__main__':
    unittest.main()
