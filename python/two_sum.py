"""
两数之和 (Two Sum)

问题描述：
给定一个整数数组 nums 和一个目标值 target，在数组中找出和为目标值的两个整数，并返回它们的索引。

使用场景：
- 查找数组中满足特定条件的元素对
- 解决类似的配对问题
- 作为更复杂算法的基础组件

算法难度：简单

时间复杂度：O(n) - 只需遍历数组一次
空间复杂度：O(n) - 使用哈希表存储已访问的元素

其他信息：
- 该算法利用哈希表的特性，将查找时间从 O(n) 降低到 O(1)
- 可以处理负数和零的情况
- 假设每个输入只对应一个答案
"""

from typing import List, Tuple


def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    """
    查找数组中两个和为目标值的元素的索引
    
    Args:
        nums: 整数数组
        target: 目标值
    
    Returns:
        两个元素的索引
    """
    # 创建哈希表，用于存储已访问的元素及其索引
    num_map = {}
    
    # 遍历数组
    for i, num in enumerate(nums):
        # 计算需要找到的补数
        complement = target - num
        
        # 如果补数在哈希表中，返回结果
        if complement in num_map:
            return (num_map[complement], i)
        
        # 否则，将当前元素及其索引加入哈希表
        num_map[num] = i
    
    # 题目假设每个输入都有一个答案，所以这里不会执行到
    raise ValueError("No two sum solution")


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([2, 7, 11, 15], 9, (0, 1)),
        ([3, 2, 4], 6, (1, 2)),
        ([3, 3], 6, (0, 1)),
        ([-1, -2, -3, -4, -5], -8, (2, 4)),
        ([0, 4, 3, 0], 0, (0, 3))
    ]
    
    for nums, target, expected in test_cases:
        result = two_sum(nums, target)
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)