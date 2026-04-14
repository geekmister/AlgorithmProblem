"""
搜索插入位置 (Search Insert Position)

问题描述：
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

使用场景：
- 有序数组的查找和插入
- 二分查找的应用
- 数据结构中的插入操作

算法难度：简单

时间复杂度：O(log n) - 使用二分查找
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 数组已经排序，这是使用二分查找的前提
- 可以使用二分查找来高效地找到目标值或插入位置
- 需要考虑数组为空的情况
"""

from typing import List


def search_insert(nums: List[int], target: int) -> int:
    """
    搜索目标值在排序数组中的位置，或返回其插入位置
    
    Args:
        nums: 排序数组
        target: 目标值
    
    Returns:
        目标值的索引或插入位置
    """
    # 初始化左右指针
    left, right = 0, len(nums) - 1
    
    # 二分查找
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # 当目标值不存在时，left就是插入位置
    return left


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([], 5, 0),
        ([1], 0, 0),
        ([1], 2, 1)
    ]
    
    for nums, target, expected in test_cases:
        result = search_insert(nums, target)
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)