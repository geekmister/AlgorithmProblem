"""
多数元素 (Majority Element)

问题描述：
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

使用场景：
- 投票系统
- 数据统计
- 模式识别

算法难度：简单

时间复杂度：O(n) - 只需遍历数组一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 可以使用摩尔投票算法（Boyer-Moore Voting Algorithm）
- 假设数组非空，且总是存在多数元素
- 摩尔投票算法的核心思想是抵消不同元素
"""

from typing import List


def majority_element(nums: List[int]) -> int:
    """
    找到数组中的多数元素
    
    Args:
        nums: 整数数组
    
    Returns:
        多数元素
    """
    # 初始化候选元素和计数
    candidate = None
    count = 0
    
    # 遍历数组
    for num in nums:
        # 如果计数为0，选择当前元素作为候选
        if count == 0:
            candidate = num
        # 更新计数
        count += 1 if num == candidate else -1
    
    # 验证候选元素是否是多数元素（题目假设存在，所以可以省略）
    # count = 0
    # for num in nums:
    #     if num == candidate:
    #         count += 1
    # return candidate if count > len(nums) // 2 else -1
    
    return candidate


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),
        ([1, 1, 1, 2, 2], 1),
        ([1, 2, 3, 4, 5, 5, 5, 5, 5], 5)
    ]
    
    for nums, expected in test_cases:
        result = majority_element(nums)
        print(f"Input: nums = {nums}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)