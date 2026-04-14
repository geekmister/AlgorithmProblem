"""
接雨水 (Trapping Rain Water)

问题描述：
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

使用场景：
- 数组操作
- 双指针技巧
- 动态规划
- 算法设计

算法难度：困难

时间复杂度：O(n) - 只需遍历数组一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 每个位置的接水量由其左侧和右侧的最大高度决定
- 可以使用双指针技巧，从两端向中间移动
- 每次移动较低的那个指针，以计算当前位置的接水量
"""

from typing import List


def trap(height: List[int]) -> int:
    """
    计算能够接的雨水量
    
    Args:
        height: 整数数组，表示每个柱子的高度
    
    Returns:
        能接的雨水量
    """
    if not height:
        return 0
    
    # 初始化双指针和最大高度
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0
    
    # 遍历数组
    while left < right:
        if left_max < right_max:
            # 移动左指针
            left += 1
            # 更新左最大高度
            left_max = max(left_max, height[left])
            # 计算当前位置的接水量
            water += left_max - height[left]
        else:
            # 移动右指针
            right -= 1
            # 更新右最大高度
            right_max = max(right_max, height[right])
            # 计算当前位置的接水量
            water += right_max - height[right]
    
    return water


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),  # 能接6单位雨水
        ([4, 2, 0, 3, 2, 5], 9),  # 能接9单位雨水
        ([0, 1, 2, 3, 4, 5], 0),  # 能接0单位雨水
        ([5, 4, 3, 2, 1, 0], 0),  # 能接0单位雨水
        ([2, 0, 2], 2)  # 能接2单位雨水
    ]
    
    for heights, expected in test_cases:
        result = trap(heights)
        print(f"Input: {heights}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)