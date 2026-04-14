"""
整数反转 (Reverse Integer)

问题描述：
给定一个 32 位有符号整数，将其数字反转。

使用场景：
- 数字处理和转换
- 密码学中的某些算法
- 验证回文数

算法难度：简单

时间复杂度：O(log n) - 数字的位数是 log10(n)
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 需要注意整数溢出的问题
- 对于 32 位有符号整数，范围是 [-2^31, 2^31 - 1]
- 当反转后的结果超出范围时，返回 0
"""


def reverse_integer(x: int) -> int:
    """
    反转整数
    
    Args:
        x: 32位有符号整数
    
    Returns:
        反转后的整数，若溢出则返回0
    """
    # 处理符号
    sign = 1 if x >= 0 else -1
    x = abs(x)
    
    # 反转数字
    reversed_num = 0
    while x > 0:
        # 取出最后一位数字
        digit = x % 10
        # 将其添加到反转结果中
        reversed_num = reversed_num * 10 + digit
        # 移除最后一位数字
        x = x // 10
    
    # 恢复符号
    reversed_num *= sign
    
    # 检查是否溢出
    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        return 0
    
    return reversed_num


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (1534236469, 0)  # 测试溢出情况
    ]
    
    for x, expected in test_cases:
        result = reverse_integer(x)
        print(f"Input: {x}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)