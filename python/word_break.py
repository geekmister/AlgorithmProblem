"""
单词拆分 (Word Break)

问题描述：
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判断 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

使用场景：
- 字符串操作
- 动态规划
- 算法设计

算法难度：中等

时间复杂度：O(n^2) - n是字符串的长度
空间复杂度：O(n) - 需要存储动态规划表

其他信息：
- 可以使用动态规划，定义dp[i]表示前i个字符是否可以被拆分
- 状态转移方程：dp[i] = dp[j] and s[j:i] in wordDict，其中j < i
"""

from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    """
    判断字符串是否可以被拆分为字典中的单词
    
    Args:
        s: 非空字符串
        word_dict: 包含非空单词的列表
    
    Returns:
        是否可以被拆分
    """
    n = len(s)
    # 初始化动态规划表
    dp = [False] * (n + 1)
    # 空字符串可以被拆分
    dp[0] = True
    
    # 填充动态规划表
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    
    return dp[n]


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ("leetcode", ["leet", "code"], True),  # 可以拆分为"leet"和"code"
        ("applepenapple", ["apple", "pen"], True),  # 可以拆分为"apple", "pen", "apple"
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),  # 无法拆分
        ("", ["a"], True),  # 空字符串可以被拆分
        ("a", ["a"], True)  # 可以拆分为"a"
    ]
    
    for s, word_dict, expected in test_cases:
        result = word_break(s, word_dict)
        print(f"Input: s={s}, wordDict={word_dict}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)