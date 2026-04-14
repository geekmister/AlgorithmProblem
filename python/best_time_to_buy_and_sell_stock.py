"""
买卖股票的最佳时机 (Best Time to Buy and Sell Stock)

问题描述：
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。设计一个算法来计算你所能获取的最大利润。

使用场景：
- 股票交易策略
- 金融分析
- 动态规划

算法难度：简单

时间复杂度：O(n) - 只需遍历数组一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 只能进行一次交易（买入和卖出各一次）
- 可以使用贪心算法，记录历史最低点
- 需要考虑股票价格一直下跌的情况（此时利润为0）
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    """
    计算买卖股票的最大利润
    
    Args:
        prices: 股票价格数组
    
    Returns:
        最大利润
    """
    # 处理空数组情况
    if not prices:
        return 0
    
    # 初始化最小价格和最大利润
    min_price = prices[0]
    max_profit = 0
    
    # 遍历数组
    for price in prices[1:]:
        # 更新最小价格
        if price < min_price:
            min_price = price
        # 计算当前利润并更新最大利润
        else:
            current_profit = price - min_price
            if current_profit > max_profit:
                max_profit = current_profit
    
    return max_profit


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),  # 买入价格1，卖出价格6，利润5
        ([7, 6, 4, 3, 1], 0),  # 价格一直下跌，利润0
        ([1, 2, 3, 4, 5], 4),  # 买入价格1，卖出价格5，利润4
        ([2, 1, 2, 1, 0, 1, 2], 2),  # 买入价格0，卖出价格2，利润2
        ([3], 0)  # 只有一天，无法交易，利润0
    ]
    
    for prices, expected in test_cases:
        result = max_profit(prices)
        print(f"Input: prices = {prices}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)