"""
跳跃游戏 II (Jump Game II)

问题描述：
给定一个非负整数数组 nums，你最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。你的目标是使用最少的跳跃次数到达数组的最后一个位置。

使用场景：
- 数组操作
- 贪心算法
- 算法设计

算法难度：中等

时间复杂度：O(n) - 只需遍历数组一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 可以使用贪心算法，维护当前的边界和下一个边界
- 每次到达当前边界时，增加跳跃次数并更新边界
"""

from typing import List


def jump(nums: List[int]) -> int:
    """
    计算到达最后一个位置所需的最少跳跃次数
    
    Args:
        nums: 非负整数数组，表示每个位置可以跳跃的最大长度
    
    Returns:
        最少跳跃次数
    """
    n = len(nums)
    if n == 1:
        return 0
    
    # 初始化跳跃次数、当前边界和下一个边界
    jumps = 0
    current_end = 0
    farthest = 0
    
    # 遍历数组
    for i in range(n - 1):
        # 更新最远可达位置
        farthest = max(farthest, i + nums[i])
        # 如果到达当前边界，增加跳跃次数并更新边界
        if i == current_end:
            jumps += 1
            current_end = farthest
            # 如果最远可达位置已经到达或超过最后一个位置，跳出循环
            if current_end >= n - 1:
                break
    
    return jumps


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([2, 3, 1, 1, 4], 2),  # 最少需要2次跳跃
        ([2, 3, 0, 1, 4], 2),  # 最少需要2次跳跃
        ([1, 1, 1, 1], 3),  # 最少需要3次跳跃
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 1),  # 最少需要1次跳跃
        ([0], 0)  # 只有一个元素，不需要跳跃
    ]
    
    for nums, expected in test_cases:
        result = jump(nums)
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)