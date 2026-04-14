"""
回文数 (Palindrome Number)

问题描述：
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

使用场景：
- 验证数字是否对称
- 密码学中的应用
- 数字处理和验证

算法难度：简单

时间复杂度：O(log n) - 数字的位数是 log10(n)
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 负数不是回文数，因为负号会导致不对称
- 可以通过反转一半数字来优化性能
- 避免了将数字转换为字符串的额外空间开销
"""


def is_palindrome(x: int) -> bool:
    """
    判断整数是否是回文数
    
    Args:
        x: 整数
    
    Returns:
        是否是回文数
    """
    # 负数不是回文数
    if x < 0:
        return False
    
    # 以0结尾的非零数字不是回文数
    if x % 10 == 0 and x != 0:
        return False
    
    # 反转一半数字
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x = x // 10
    
    # 当数字长度为奇数时，去掉中间的数字
    return x == reversed_half or x == reversed_half // 10


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (12321, True),
        (1234321, True),
        (12345, False)
    ]
    
    for x, expected in test_cases:
        result = is_palindrome(x)
        print(f"Input: {x}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)