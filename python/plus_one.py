"""
加一 (Plus One)

问题描述：
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

使用场景：
- 数字处理
- 大整数运算
- 计数器实现

算法难度：简单

时间复杂度：O(n) - 最坏情况下需要遍历整个数组
空间复杂度：O(1) - 只使用常数级别的额外空间（除了返回的数组）

其他信息：
- 数组的每个元素只存储单个数字
- 最高位数字存放在数组的首位
- 需要考虑进位的情况，特别是当所有数字都是9时
"""

from typing import List


def plus_one(digits: List[int]) -> List[int]:
    """
    对由数组表示的非负整数加一
    
    Args:
        digits: 表示非负整数的数组
    
    Returns:
        加一后的数组
    """
    # 从最后一位开始处理
    for i in range(len(digits) - 1, -1, -1):
        # 如果当前位小于9，直接加一返回
        if digits[i] < 9:
            digits[i] += 1
            return digits
        # 否则，当前位变为0，继续处理前一位
        digits[i] = 0
    
    # 如果所有位都是9，需要在最前面添加1
    return [1] + digits


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([9], [1, 0]),
        ([9, 9, 9], [1, 0, 0, 0]),
        ([0], [1]),
        ([5, 6, 7, 8], [5, 6, 7, 9])
    ]
    
    for digits, expected in test_cases:
        # 复制数组用于验证
        original_digits = digits.copy()
        result = plus_one(digits)
        print(f"Input: {original_digits}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)