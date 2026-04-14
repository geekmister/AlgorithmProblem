"""
编辑距离 (Edit Distance)

问题描述：
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数。

使用场景：
- 字符串操作
- 动态规划
- 算法设计

算法难度：困难

时间复杂度：O(mn) - m和n分别是两个单词的长度
空间复杂度：O(mn) - 需要存储动态规划表

其他信息：
- 可以进行的操作有三种：插入一个字符、删除一个字符、替换一个字符
- 可以使用动态规划，定义dp[i][j]表示word1的前i个字符转换成word2的前j个字符所需的最少操作数
- 状态转移方程：
  - 如果word1[i-1] == word2[j-1]，则dp[i][j] = dp[i-1][j-1]
  - 否则，dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
"""

from typing import List


def min_distance(word1: str, word2: str) -> int:
    """
    计算将word1转换成word2所使用的最少操作数
    
    Args:
        word1: 第一个单词
        word2: 第二个单词
    
    Returns:
        最少操作数
    """
    m, n = len(word1), len(word2)
    
    # 初始化动态规划表
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 边界条件：一个单词为空，需要插入另一个单词的所有字符
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # 填充动态规划表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                # 如果当前字符相同，不需要操作
                dp[i][j] = dp[i-1][j-1]
            else:
                # 否则，取三种操作中的最小值加1
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    
    return dp[m][n]


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ("horse", "ros", 3),  # 需要3次操作：h→r, 删除r, e→s
        ("intention", "execution", 5),  # 需要5次操作
        ("", "a", 1),  # 需要1次插入操作
        ("a", "", 1),  # 需要1次删除操作
        ("a", "a", 0)  # 不需要操作
    ]
    
    for word1, word2, expected in test_cases:
        result = min_distance(word1, word2)
        print(f"Input: word1={word1}, word2={word2}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)