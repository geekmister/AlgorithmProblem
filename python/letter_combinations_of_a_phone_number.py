"""
电话号码的字母组合 (Letter Combinations of a Phone Number)

问题描述：
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

使用场景：
- 字符串操作
- 算法设计
- 回溯算法

算法难度：中等

时间复杂度：O(4^n) - n是输入字符串的长度，每个数字最多对应4个字母
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 数字到字母的映射与电话按键相同
- 例如，2对应abc，3对应def，等等
- 可以使用回溯算法，遍历所有可能的组合
"""

from typing import List


def letter_combinations(digits: str) -> List[str]:
    """
    生成电话号码的字母组合
    
    Args:
        digits: 包含数字2-9的字符串
    
    Returns:
        所有可能的字母组合
    """
    # 数字到字母的映射
    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    # 处理空字符串的情况
    if not digits:
        return []
    
    result = []
    
    # 回溯函数
    def backtrack(index, current):
        # 如果已经处理完所有数字，将当前组合添加到结果中
        if index == len(digits):
            result.append(current)
            return
        
        # 遍历当前数字对应的所有字母
        for char in phone_map[digits[index]]:
            # 递归处理下一个数字
            backtrack(index + 1, current + char)
    
    # 开始回溯
    backtrack(0, '')
    
    return result


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),  # 所有可能的组合
        ("", []),  # 空字符串
        ("2", ["a", "b", "c"]),  # 只有一个数字
        ("9", ["w", "x", "y", "z"])  # 数字9对应4个字母
    ]
    
    for digits, expected in test_cases:
        result = letter_combinations(digits)
        # 排序后比较，因为顺序可能不同
        result.sort()
        expected.sort()
        print(f"Input: {digits}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)