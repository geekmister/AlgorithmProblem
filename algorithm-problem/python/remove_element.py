"""
移除元素 (Remove Element)

问题描述：
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

使用场景：
- 数组元素的过滤
- 数据清理
- 内存使用优化

算法难度：简单

时间复杂度：O(n) - 只需遍历数组一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 使用双指针技术，一个指针用于遍历，一个指针用于记录非目标值元素的位置
- 需要在原地修改数组，不能使用额外的数组空间
- 元素的顺序可以改变
"""

from typing import List


def remove_element(nums: List[int], val: int) -> int:
    """
    移除数组中所有等于val的元素
    
    Args:
        nums: 数组
        val: 要移除的值
    
    Returns:
        移除后数组的新长度
    """
    # 慢指针，记录非val元素的位置
    slow = 0
    
    # 快指针，遍历数组
    for fast in range(len(nums)):
        # 如果当前元素不等于val，将其移到慢指针位置
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    
    return slow


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([3, 2, 2, 3], 3, 2, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]),
        ([], 0, 0, []),
        ([1], 1, 0, []),
        ([1, 2, 3, 4, 5], 6, 5, [1, 2, 3, 4, 5])
    ]
    
    for nums, val, expected_length, expected_nums in test_cases:
        # 复制数组用于验证
        original_nums = nums.copy()
        length = remove_element(nums, val)
        # 验证长度是否正确
        length_correct = length == expected_length
        # 验证数组前length个元素是否正确（不考虑顺序）
        # 因为元素顺序可以改变，所以需要排序后比较
        nums_correct = sorted(nums[:length]) == sorted(expected_nums)
        
        print(f"Input: nums = {original_nums}, val = {val}")
        print(f"Expected Length: {expected_length}")
        print(f"Expected Nums: {expected_nums}")
        print(f"Result Length: {length}")
        print(f"Result Nums: {nums[:length]}")
        print(f"Pass: {length_correct and nums_correct}")
        print("-" * 50)