"""
跳跃游戏 (Jump Game)

问题描述：
给定一个非负整数数组 nums，你最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。判断你是否能够到达最后一个位置。

使用场景：
- 数组操作
- 贪心算法
- 算法设计

算法难度：中等

时间复杂度：O(n) - 只需遍历数组一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 可以使用贪心算法，维护一个最远可达位置
- 每次更新最远可达位置，直到到达最后一个位置或无法继续前进
"""

from typing import List


def can_jump(nums: List[int]) -> bool:
    """
    判断是否能够到达最后一个位置
    
    Args:
        nums: 非负整数数组，表示每个位置可以跳跃的最大长度
    
    Returns:
        是否能够到达最后一个位置
    """
    # 初始化最远可达位置
    max_reach = 0
    n = len(nums)
    
    # 遍历数组
    for i in range(n):
        # 如果当前位置超过了最远可达位置，返回False
        if i > max_reach:
            return False
        # 更新最远可达位置
        max_reach = max(max_reach, i + nums[i])
        # 如果最远可达位置已经到达或超过最后一个位置，返回True
        if max_reach >= n - 1:
            return True
    
    return True


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([2, 3, 1, 1, 4], True),  # 可以到达最后一个位置
        ([3, 2, 1, 0, 4], False),  # 无法到达最后一个位置
        ([0], True),  # 只有一个元素，已经到达
        ([1, 2, 3], True),  # 可以到达最后一个位置
        ([1, 0, 1, 0], False)  # 无法到达最后一个位置
    ]
    
    for nums, expected in test_cases:
        result = can_jump(nums)
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)