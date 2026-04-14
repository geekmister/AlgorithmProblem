"""
最小路径和 (Minimum Path Sum)

问题描述：
给定一个包含非负整数的 m x n 网格 grid，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

使用场景：
- 矩阵操作
- 算法设计
- 动态规划

算法难度：中等

时间复杂度：O(m * n) - m和n是网格的行数和列数
空间复杂度：O(m * n) - 需要存储动态规划表

其他信息：
- 每次只能向下或者向右移动一步
- 可以使用动态规划，定义dp[i][j]表示从左上角到(i,j)的最小路径和
- 状态转移方程：dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
"""

from typing import List


def min_path_sum(grid: List[List[int]]) -> int:
    """
    计算从左上角到右下角的最小路径和
    
    Args:
        grid: 包含非负整数的二维网格
    
    Returns:
        最小路径和
    """
    m, n = len(grid), len(grid[0])
    
    # 初始化动态规划表
    dp = [[0] * n for _ in range(m)]
    
    # 初始化第一个元素
    dp[0][0] = grid[0][0]
    
    # 初始化第一行
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # 初始化第一列
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # 填充动态规划表
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    
    # 返回右下角的最小路径和
    return dp[-1][-1]


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        (
            [
                [1, 3, 1],
                [1, 5, 1],
                [4, 2, 1]
            ],
            7
        ),  # 最小路径和是7（1→3→1→1→1）
        (
            [
                [1, 2, 3],
                [4, 5, 6]
            ],
            12
        ),  # 最小路径和是12（1→2→3→6）
        (
            [[1]],
            1
        ),  # 只有一个元素
        (
            [
                [1, 2],
                [1, 1]
            ],
            3
        )  # 最小路径和是3（1→2→1 或 1→1→1）
    ]
    
    for grid, expected in test_cases:
        result = min_path_sum(grid)
        print(f"Input: {grid}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)