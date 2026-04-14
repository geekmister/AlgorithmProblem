"""
最长回文子串 (Longest Palindromic Substring)

问题描述：
给定一个字符串 s，找到 s 中最长的回文子串。

使用场景：
- 字符串操作
- 算法设计
- 动态规划

算法难度：中等

时间复杂度：O(n^2) - n是字符串的长度
空间复杂度：O(n^2) - 动态规划表的大小

其他信息：
- 回文子串是指正着读和倒着读都一样的字符串
- 可以使用动态规划，定义dp[i][j]表示从i到j的子串是否是回文
- 也可以使用中心扩展法，从每个字符或两个字符之间开始扩展
"""

from typing import Optional


def longest_palindromic_substring(s: str) -> str:
    """
    找到最长回文子串
    
    Args:
        s: 输入字符串
    
    Returns:
        最长回文子串
    """
    n = len(s)
    if n < 2:
        return s
    
    # 初始化动态规划表
    dp = [[False] * n for _ in range(n)]
    max_length = 1
    start = 0
    
    # 单个字符都是回文
    for i in range(n):
        dp[i][i] = True
    
    # 处理长度为2的子串
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            max_length = 2
            start = i
    
    # 处理长度大于2的子串
    for length in range(3, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            # 如果首尾字符相等，且中间的子串是回文，则整个子串是回文
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                if length > max_length:
                    max_length = length
                    start = i
    
    # 返回最长回文子串
    return s[start:start+max_length]


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ("babad", "bab"),  # 最长回文子串是"bab"或"aba"
        ("cbbd", "bb"),  # 最长回文子串是"bb"
        ("a", "a"),  # 最长回文子串是"a"
        ("ac", "a"),  # 最长回文子串是"a"或"c"
        ("racecar", "racecar")  # 最长回文子串是"racecar"
    ]
    
    for s, expected in test_cases:
        result = longest_palindromic_substring(s)
        # 检查结果是否是回文，并且长度是否正确
        is_palindrome = result == result[::-1]
        has_correct_length = len(result) == len(expected)
        print(f"Input: {s}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {is_palindrome and has_correct_length}")
        print("-" * 50)