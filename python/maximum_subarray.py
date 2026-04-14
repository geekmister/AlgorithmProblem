"""
最大子序和 (Maximum Subarray)

问题描述：
给定一个整数数组 nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

使用场景：
- 数组操作
- 动态规划
- 算法设计

算法难度：简单

时间复杂度：O(n) - 只需遍历数组一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 可以使用动态规划，定义dp[i]表示以第i个元素结尾的最大子序和
- 状态转移方程：dp[i] = max(nums[i], dp[i-1] + nums[i])
- 可以使用贪心算法，维护当前的最大和
"""

from typing import List


def max_subarray(nums: List[int]) -> int:
    """
    计算最大子序和
    
    Args:
        nums: 整数数组
    
    Returns:
        最大子序和
    """
    if not nums:
        return 0
    
    # 初始化当前最大和和全局最大和
    current_max = nums[0]
    global_max = nums[0]
    
    # 遍历数组
    for i in range(1, len(nums)):
        # 更新当前最大和
        current_max = max(nums[i], current_max + nums[i])
        # 更新全局最大和
        global_max = max(global_max, current_max)
    
    return global_max


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),  # 最大子序和是6（4, -1, 2, 1）
        ([1], 1),  # 只有一个元素
        ([5, 4, -1, 7, 8], 23),  # 最大子序和是23（5, 4, -1, 7, 8）
        ([-1, -2, -3, -4], -1),  # 所有元素都是负数
        ([0, -1, 2, -3, 4], 4)  # 最大子序和是4（4）
    ]
    
    for nums, expected in test_cases:
        result = max_subarray(nums)
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)