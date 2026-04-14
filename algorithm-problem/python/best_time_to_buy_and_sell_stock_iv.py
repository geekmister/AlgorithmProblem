"""
买卖股票的最佳时机 IV (Best Time to Buy and Sell Stock IV)

问题描述：
给定一个整数 k 和一个整数数组 prices，其中 prices[i] 是某支给定的股票在第 i 天的价格。设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

使用场景：
- 数组操作
- 动态规划
- 算法设计

算法难度：困难

时间复杂度：O(nk) - n是数组的长度，k是交易次数
空间复杂度：O(nk) - 需要存储动态规划表

其他信息：
- 可以使用动态规划，定义dp[i][j][0]表示第i天，已经进行了j笔交易，且当前不持有股票的最大利润
- 定义dp[i][j][1]表示第i天，已经进行了j笔交易，且当前持有股票的最大利润
- 状态转移方程：
  - dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
  - dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
"""

from typing import List


def max_profit(k: int, prices: List[int]) -> int:
    """
    计算最多完成k笔交易的最大利润
    
    Args:
        k: 最多可以完成的交易次数
        prices: 股票价格数组
    
    Returns:
        最大利润
    """
    if not prices:
        return 0
    
    n = len(prices)
    # 如果k大于等于n/2，相当于可以进行无限次交易
    if k >= n // 2:
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
    
    # 初始化动态规划表
    dp = [[[0] * 2 for _ in range(k+1)] for __ in range(n)]
    
    # 初始化边界条件
    for j in range(k+1):
        dp[0][j][1] = -prices[0]
    
    # 遍历数组
    for i in range(1, n):
        for j in range(1, k+1):
            # 不持有股票的状态
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
            # 持有股票的状态
            dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
    
    return dp[-1][k][0]


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        (2, [2, 4, 1], 2),  # 最大利润是2（2买入，4卖出）
        (2, [3, 2, 6, 5, 0, 3], 7),  # 最大利润是7（2买入，6卖出，0买入，3卖出）
        (1, [7, 6, 4, 3, 1], 0),  # 没有利润
        (0, [1, 2, 3, 4, 5], 0),  # 不能交易
        (3, [3, 3, 5, 0, 0, 3, 1, 4], 8)  # 最大利润是8（0买入，3卖出，1买入，4卖出）
    ]
    
    for k, prices, expected in test_cases:
        result = max_profit(k, prices)
        print(f"Input: k={k}, prices={prices}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)