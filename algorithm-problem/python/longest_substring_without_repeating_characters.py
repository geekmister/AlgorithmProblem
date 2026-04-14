"""
最长无重复字符的子串 (Longest Substring Without Repeating Characters)

问题描述：
给定一个字符串 s，找出其中不含有重复字符的最长子串的长度。

使用场景：
- 字符串操作
- 算法设计
- 滑动窗口

算法难度：中等

时间复杂度：O(n) - n是字符串的长度
空间复杂度：O(1) - 字符集的大小是有限的

其他信息：
- 可以使用滑动窗口算法，维护一个窗口，窗口内的字符都是唯一的
- 使用哈希表或数组来记录字符出现的位置
- 当遇到重复字符时，移动窗口的左边界
"""

from typing import Dict


def length_of_longest_substring(s: str) -> int:
    """
    找出最长无重复字符的子串的长度
    
    Args:
        s: 输入字符串
    
    Returns:
        最长无重复字符的子串的长度
    """
    # 哈希表，记录字符最后出现的位置
    char_index: Dict[str, int] = {}
    max_length = 0
    left = 0
    
    # 遍历字符串
    for right in range(len(s)):
        # 如果字符已经在哈希表中，并且位置在当前窗口内，移动左边界
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        
        # 更新字符最后出现的位置
        char_index[s[right]] = right
        
        # 更新最大长度
        max_length = max(max_length, right - left + 1)
    
    return max_length


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ("abcabcbb", 3),  # 最长无重复字符的子串是"abc"，长度为3
        ("bbbbb", 1),  # 最长无重复字符的子串是"b"，长度为1
        ("pwwkew", 3),  # 最长无重复字符的子串是"wke"，长度为3
        ("", 0),  # 空字符串，长度为0
        ("au", 2)  # 最长无重复字符的子串是"au"，长度为2
    ]
    
    for s, expected in test_cases:
        result = length_of_longest_substring(s)
        print(f"Input: {s}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)