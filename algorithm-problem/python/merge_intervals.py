"""
合并区间 (Merge Intervals)

问题描述：
给定一个区间的集合 intervals，其中 intervals[i] = [starti, endi]，合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

使用场景：
- 数组操作
- 排序算法
- 算法设计

算法难度：中等

时间复杂度：O(n log n) - 排序的时间复杂度
空间复杂度：O(n) - 需要存储合并后的区间

其他信息：
- 可以先对区间按照起始位置进行排序
- 然后遍历排序后的区间，合并重叠的区间
"""

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    合并所有重叠的区间
    
    Args:
        intervals: 区间的集合
    
    Returns:
        不重叠的区间数组
    """
    if not intervals:
        return []
    
    # 按照起始位置对区间进行排序
    intervals.sort(key=lambda x: x[0])
    
    # 初始化结果数组
    merged = [intervals[0]]
    
    # 遍历排序后的区间
    for interval in intervals[1:]:
        # 获取结果数组中的最后一个区间
        last = merged[-1]
        # 如果当前区间与最后一个区间重叠，合并它们
        if interval[0] <= last[1]:
            merged[-1] = [last[0], max(last[1], interval[1])]
        else:
            # 否则，将当前区间添加到结果数组中
            merged.append(interval)
    
    return merged


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),  # 合并重叠的区间
        ([[1, 4], [4, 5]], [[1, 5]]),  # 合并相邻的区间
        ([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]),  # 没有重叠的区间
        ([[1, 5], [2, 3], [4, 6], [7, 8]], [[1, 6], [7, 8]]),  # 多个重叠的区间
        ([], [])  # 空数组
    ]
    
    for intervals, expected in test_cases:
        result = merge(intervals)
        print(f"Input: {intervals}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)