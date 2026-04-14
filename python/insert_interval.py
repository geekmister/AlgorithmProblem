"""
插入区间 (Insert Interval)

问题描述：
给定一个无重叠的，按照区间起始端点排序的区间列表 intervals，以及一个新的区间 newInterval，将 newInterval 插入到 intervals 中，使得插入后的区间仍然保持无重叠且按照起始端点排序。

使用场景：
- 数组操作
- 排序算法
- 算法设计

算法难度：中等

时间复杂度：O(n) - 只需遍历数组一次
空间复杂度：O(n) - 需要存储结果数组

其他信息：
- 可以遍历区间列表，找到需要插入的位置
- 合并与 newInterval 重叠的区间
"""

from typing import List


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """
    插入新的区间并合并重叠的区间
    
    Args:
        intervals: 无重叠的，按照区间起始端点排序的区间列表
        new_interval: 新的区间
    
    Returns:
        插入后的区间列表
    """
    result = []
    i = 0
    n = len(intervals)
    
    # 添加所有在 new_interval 之前的区间
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    
    # 合并与 new_interval 重叠的区间
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    
    # 添加合并后的区间
    result.append(new_interval)
    
    # 添加剩余的区间
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([], [1, 2], [[1, 2]]),  # 空数组
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),  # 插入并合并
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),  # 插入并合并多个区间
        ([[1, 5]], [2, 3], [[1, 5]]),  # 新区间被包含
        ([[1, 5]], [6, 7], [[1, 5], [6, 7]]),  # 新区间在末尾
        ([[1, 5]], [0, 0], [[0, 0], [1, 5]])  # 新区间在开头
    ]
    
    for intervals, new_interval, expected in test_cases:
        result = insert(intervals, new_interval)
        print(f"Input: intervals={intervals}, newInterval={new_interval}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)