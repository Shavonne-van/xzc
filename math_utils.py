# math_utils.py
def add(a: int, b: int) -> int:
    """加法函数"""
    return a + b

def factorial(n: int) -> int:
    """阶乘函数（n≥0）"""
    if n < 0:
        raise ValueError("n 不能为负数")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result