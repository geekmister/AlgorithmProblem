"""
合并两个有序数组 (Merge Sorted Array)

问题描述：
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

使用场景：
- 归并排序中的合并操作
- 数据合并
- 有序数组的处理

算法难度：简单

时间复杂度：O(n+m) - n和m分别是两个数组的长度
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素
- 从后向前合并可以避免覆盖 nums1 中的元素
- 需要考虑其中一个数组为空的情况
"""

from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    合并两个有序数组
    
    Args:
        nums1: 第一个有序数组，有足够的空间
        m: nums1中元素的数量
        nums2: 第二个有序数组
        n: nums2中元素的数量
    
    Returns:
        None，直接修改nums1
    """
    # 初始化指针
    p1 = m - 1  # nums1的最后一个元素
    p2 = n - 1  # nums2的最后一个元素
    p = m + n - 1  # 合并后数组的最后一个位置
    
    # 从后向前合并
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # 处理nums2中剩余的元素
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6])
    ]
    
    for nums1, m, nums2, n, expected in test_cases:
        # 复制数组用于验证
        original_nums1 = nums1.copy()
        merge(nums1, m, nums2, n)
        print(f"Input: nums1 = {original_nums1}, m = {m}, nums2 = {nums2}, n = {n}")
        print(f"Expected: {expected}")
        print(f"Result: {nums1}")
        print(f"Pass: {nums1 == expected}")
        print("-" * 50)