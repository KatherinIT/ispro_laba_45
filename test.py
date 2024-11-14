import unittest

def perimeter(a, b):
    return 2 * (a + b)

class RectanglePerimeterTestCase(unittest.TestCase):
    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_normal_perimeter(self):
        res = perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_square_perimeter(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

if __name__ == '__main__':
    unittest.main()
 