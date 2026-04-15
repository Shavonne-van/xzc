# test_math_utils.py
import unittest
from math_utils import add, factorial

class TestMathUtils(unittest.TestCase):
    # 测试加法函数
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    # 测试阶乘函数
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 7)
        self.assertEqual(factorial(3), 6)

    # 测试负数输入异常
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

# 本地直接运行测试的入口
if __name__ == '__main__':
    unittest.main()
