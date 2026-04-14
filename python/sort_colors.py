"""
颜色分类 (Sort Colors)

问题描述：
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色的顺序排列。

使用场景：
- 数组操作
- 排序算法
- 双指针技巧
- 算法设计

算法难度：中等

时间复杂度：O(n) - 只需遍历数组一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 可以使用荷兰国旗算法（Dutch National Flag Algorithm）
- 使用三个指针：left 指向0的右边界，mid 指向当前元素，right 指向2的左边界
- 遍历数组，根据当前元素的值进行交换
"""

from typing import List


def sort_colors(nums: List[int]) -> None:
    """
    原地对颜色进行排序
    
    Args:
        nums: 包含0、1、2的整数数组
    
    Returns:
        None - 原地修改数组
    """
    # 初始化三个指针
    left = 0  # 0的右边界
    mid = 0  # 当前元素
    right = len(nums) - 1  # 2的左边界
    
    # 遍历数组
    while mid <= right:
        if nums[mid] == 0:
            # 如果当前元素是0，交换到左侧
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            # 如果当前元素是1，继续遍历
            mid += 1
        else:
            # 如果当前元素是2，交换到右侧
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),  # 排序后的数组
        ([2, 0, 1], [0, 1, 2]),  # 排序后的数组
        ([0], [0]),  # 只有一个元素
        ([1], [1]),  # 只有一个元素
        ([2, 2, 2, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 2, 2, 2])  # 排序后的数组
    ]
    
    for nums, expected in test_cases:
        # 创建副本，避免修改原始测试用例
        nums_copy = nums.copy()
        sort_colors(nums_copy)
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Result: {nums_copy}")
        print(f"Pass: {nums_copy == expected}")
        print("-" * 50)