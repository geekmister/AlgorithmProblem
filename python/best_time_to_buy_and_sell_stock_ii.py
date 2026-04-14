"""
买卖股票的最佳时机 II (Best Time to Buy and Sell Stock II)

问题描述：
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

使用场景：
- 股票交易策略
- 金融分析
- 贪心算法

算法难度：简单

时间复杂度：O(n) - 只需遍历数组一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 可以进行多次交易，但不能同时参与多笔交易（必须在再次购买前出售掉之前的股票）
- 可以使用贪心算法，只要今天的价格比昨天高，就进行交易
- 这种策略可以捕获所有的价格上涨
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    """
    计算买卖股票的最大利润（可以多次交易）
    
    Args:
        prices: 股票价格数组
    
    Returns:
        最大利润
    """
    # 处理空数组情况
    if not prices:
        return 0
    
    # 初始化最大利润
    max_profit = 0
    
    # 遍历数组，只要今天的价格比昨天高，就进行交易
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]
    
    return max_profit


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 7),  # 交易：1->5, 3->6，利润4+3=7
        ([1, 2, 3, 4, 5], 4),  # 交易：1->2->3->4->5，利润4
        ([7, 6, 4, 3, 1], 0),  # 价格一直下跌，不进行交易
        ([3, 2, 6, 5, 0, 3], 7),  # 交易：2->6, 0->3，利润4+3=7
        ([2, 1, 2, 0, 1], 2)  # 交易：1->2, 0->1，利润1+1=2
    ]
    
    for prices, expected in test_cases:
        result = max_profit(prices)
        print(f"Input: prices = {prices}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)