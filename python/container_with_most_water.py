"""
盛最多水的容器 (Container With Most Water)

问题描述：
给定一个长度为 n 的整数数组 height，其中每个元素表示坐标 (i, height[i]) 处的点。找出两条直线，使得它们与 x 轴共同构成的容器能够容纳最多的水。

使用场景：
- 数组操作
- 双指针技巧
- 算法设计

算法难度：中等

时间复杂度：O(n) - 只需遍历数组一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 容器的容量由较短的那条直线决定
- 可以使用双指针技巧，从两端向中间移动
- 每次移动较短的那条直线，以寻找更大的容量
"""

from typing import List


def max_area(height: List[int]) -> int:
    """
    计算容器能够容纳的最大水量
    
    Args:
        height: 整数数组，表示每个坐标处的高度
    
    Returns:
        最大水量
    """
    # 初始化双指针和最大面积
    left, right = 0, len(height) - 1
    max_area = 0
    
    # 遍历数组
    while left < right:
        # 计算当前容量
        current_area = min(height[left], height[right]) * (right - left)
        # 更新最大面积
        max_area = max(max_area, current_area)
        
        # 移动较短的那条直线
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),  # 最大水量是49
        ([1, 1], 1),  # 最大水量是1
        ([4, 3, 2, 1, 4], 16),  # 最大水量是16
        ([1, 2, 1], 2),  # 最大水量是2
        ([2, 3, 4, 5, 18, 17, 6], 17)  # 最大水量是17
    ]
    
    for heights, expected in test_cases:
        result = max_area(heights)
        print(f"Input: {heights}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)