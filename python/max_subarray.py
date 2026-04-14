"""
最大子序和 (Maximum Subarray)

问题描述：
给定一个整数数组 nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

使用场景：
- 金融分析中的股票价格分析
- 信号处理
- 数据挖掘

算法难度：简单

时间复杂度：O(n) - 只需遍历数组一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 该问题可以使用动态规划的思想解决
- 关键在于维护两个变量：当前子数组的和和最大子数组的和
- 当当前子数组的和小于0时，重新开始计算子数组
"""

from typing import List


def max_subarray(nums: List[int]) -> int:
    """
    找到具有最大和的连续子数组
    
    Args:
        nums: 整数数组
    
    Returns:
        最大子数组的和
    """
    # 处理空数组情况
    if not nums:
        return 0
    
    # 初始化当前子数组的和和最大子数组的和
    current_sum = max_sum = nums[0]
    
    # 遍历数组
    for num in nums[1:]:
        # 更新当前子数组的和：如果当前子数组的和小于0，则重新开始
        current_sum = max(num, current_sum + num)
        # 更新最大子数组的和
        max_sum = max(max_sum, current_sum)
    
    return max_sum


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),  # 子数组 [4, -1, 2, 1]
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-1], -1),
        ([-100000], -100000),
        ([1, -1, 1, -1, 1], 1)
    ]
    
    for nums, expected in test_cases:
        result = max_subarray(nums)
        print(f"Input: nums = {nums}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)