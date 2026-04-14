"""
买卖股票的最佳时机 III (Best Time to Buy and Sell Stock III)

问题描述：
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。设计一个算法来计算你所能获取的最大利润。你最多可以完成两笔交易。

使用场景：
- 数组操作
- 动态规划
- 算法设计

算法难度：困难

时间复杂度：O(n) - 只需遍历数组一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 可以使用动态规划，定义四个状态：第一次买入后的最大利润、第一次卖出后的最大利润、第二次买入后的最大利润、第二次卖出后的最大利润
- 状态转移方程：
  - buy1 = max(buy1, -prices[i])
  - sell1 = max(sell1, buy1 + prices[i])
  - buy2 = max(buy2, sell1 - prices[i])
  - sell2 = max(sell2, buy2 + prices[i])
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    """
    计算最多完成两笔交易的最大利润
    
    Args:
        prices: 股票价格数组
    
    Returns:
        最大利润
    """
    if not prices:
        return 0
    
    # 初始化四个状态
    buy1 = -prices[0]  # 第一次买入后的最大利润
    sell1 = 0  # 第一次卖出后的最大利润
    buy2 = -prices[0]  # 第二次买入后的最大利润
    sell2 = 0  # 第二次卖出后的最大利润
    
    # 遍历数组
    for price in prices[1:]:
        # 更新第一次买入后的最大利润
        buy1 = max(buy1, -price)
        # 更新第一次卖出后的最大利润
        sell1 = max(sell1, buy1 + price)
        # 更新第二次买入后的最大利润
        buy2 = max(buy2, sell1 - price)
        # 更新第二次卖出后的最大利润
        sell2 = max(sell2, buy2 + price)
    
    return sell2


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([3, 3, 5, 0, 0, 3, 1, 4], 6),  # 最大利润是6（0买入，3卖出，1买入，4卖出）
        ([1, 2, 3, 4, 5], 4),  # 最大利润是4（1买入，5卖出）
        ([7, 6, 4, 3, 1], 0),  # 没有利润
        ([1], 0),  # 只有一天，无法交易
        ([1, 2, 4, 2, 5, 7, 2, 4, 9, 0], 13)  # 最大利润是13（1买入，7卖出，2买入，9卖出）
    ]
    
    for prices, expected in test_cases:
        result = max_profit(prices)
        print(f"Input: {prices}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)