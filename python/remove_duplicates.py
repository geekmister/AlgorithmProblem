"""
删除排序数组中的重复项 (Remove Duplicates from Sorted Array)

问题描述：
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

使用场景：
- 数据去重
- 数组处理和优化
- 内存使用优化

算法难度：简单

时间复杂度：O(n) - 只需遍历数组一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 数组已经排序，这是解决问题的关键
- 使用双指针技术，一个指针用于遍历，一个指针用于记录非重复元素的位置
- 需要在原地修改数组，不能使用额外的数组空间
"""

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    删除排序数组中的重复项
    
    Args:
        nums: 排序数组
    
    Returns:
        移除重复元素后的数组长度
    """
    # 处理空数组情况
    if not nums:
        return 0
    
    # 慢指针，记录非重复元素的位置
    slow = 1
    
    # 快指针，遍历数组
    for fast in range(1, len(nums)):
        # 如果当前元素与前一个元素不同，将其移到慢指针位置
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
    
    return slow


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([], 0, []),
        ([1], 1, [1]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5])
    ]
    
    for nums, expected_length, expected_nums in test_cases:
        # 复制数组用于验证
        original_nums = nums.copy()
        length = remove_duplicates(nums)
        # 验证长度是否正确
        length_correct = length == expected_length
        # 验证数组前length个元素是否正确
        nums_correct = nums[:length] == expected_nums
        
        print(f"Input: {original_nums}")
        print(f"Expected Length: {expected_length}")
        print(f"Expected Nums: {expected_nums}")
        print(f"Result Length: {length}")
        print(f"Result Nums: {nums[:length]}")
        print(f"Pass: {length_correct and nums_correct}")
        print("-" * 50)