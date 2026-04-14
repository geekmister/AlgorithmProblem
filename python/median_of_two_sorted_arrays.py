"""
寻找两个正序数组的中位数 (Median of Two Sorted Arrays)

问题描述：
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

使用场景：
- 数组操作
- 算法设计
- 二分查找

算法难度：困难

时间复杂度：O(log(min(m, n))) - 使用二分查找
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 中位数是将数组分为两个长度相等的部分的中间值
- 可以使用二分查找来找到两个数组的分割点
- 确保左半部分的所有元素都小于或等于右半部分的所有元素
"""

from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    寻找两个正序数组的中位数
    
    Args:
        nums1: 第一个正序数组
        nums2: 第二个正序数组
    
    Returns:
        两个正序数组的中位数
    """
    # 确保nums1是较短的数组，这样可以减少二分查找的次数
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    total_length = m + n
    half_length = (total_length + 1) // 2
    
    # 二分查找的范围
    left, right = 0, m
    
    while left < right:
        # 计算nums1的分割点
        i = (left + right) // 2
        # 计算nums2的分割点
        j = half_length - i
        
        # 如果nums1的分割点右侧的元素小于nums2的分割点左侧的元素，说明nums1的分割点需要右移
        if nums1[i] < nums2[j-1]:
            left = i + 1
        else:
            right = i
    
    # 最终的分割点
    i = left
    j = half_length - i
    
    # 计算左半部分的最大值
    max_left = max(
        nums1[i-1] if i > 0 else float('-inf'),
        nums2[j-1] if j > 0 else float('-inf')
    )
    
    # 如果总长度是奇数，返回左半部分的最大值
    if total_length % 2 == 1:
        return max_left
    
    # 计算右半部分的最小值
    min_right = min(
        nums1[i] if i < m else float('inf'),
        nums2[j] if j < n else float('inf')
    )
    
    # 如果总长度是偶数，返回左半部分的最大值和右半部分的最小值的平均值
    return (max_left + min_right) / 2


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([1, 3], [2], 2.0),  # 合并后 [1,2,3]，中位数是2
        ([1, 2], [3, 4], 2.5),  # 合并后 [1,2,3,4]，中位数是(2+3)/2=2.5
        ([0, 0], [0, 0], 0.0),  # 合并后 [0,0,0,0]，中位数是0
        ([], [1], 1.0),  # 合并后 [1]，中位数是1
        ([2], [], 2.0)  # 合并后 [2]，中位数是2
    ]
    
    for nums1, nums2, expected in test_cases:
        result = find_median_sorted_arrays(nums1, nums2)
        print(f"Input: nums1={nums1}, nums2={nums2}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {abs(result - expected) < 1e-6}")
        print("-" * 50)