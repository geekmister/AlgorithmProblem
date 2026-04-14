"""
三数之和 (3Sum)

问题描述：
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0？请你找出所有和为 0 且不重复的三元组。

使用场景：
- 数组操作
- 算法设计
- 双指针技巧

算法难度：中等

时间复杂度：O(n^2) - n是数组的长度
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 结果中不允许包含重复的三元组
- 可以使用排序和双指针的方法
- 首先对数组进行排序，然后遍历每个元素，使用双指针查找另外两个元素
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    找出所有和为0且不重复的三元组
    
    Args:
        nums: 输入数组
    
    Returns:
        所有和为0且不重复的三元组
    """
    # 对数组进行排序
    nums.sort()
    result = []
    n = len(nums)
    
    # 遍历每个元素作为第一个元素
    for i in range(n):
        # 避免重复的第一个元素
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # 双指针查找另外两个元素
        left = i + 1
        right = n - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total < 0:
                # 和太小，移动左指针
                left += 1
            elif total > 0:
                # 和太大，移动右指针
                right -= 1
            else:
                # 找到一个三元组
                result.append([nums[i], nums[left], nums[right]])
                
                # 避免重复的左指针元素
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                # 避免重复的右指针元素
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                
                # 移动两个指针
                left += 1
                right -= 1
    
    return result


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),  # 两个三元组
        ([], []),  # 空数组
        ([0], []),  # 只有一个元素的数组
        ([0, 0, 0], [[0, 0, 0]]),  # 三个零
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]])  # 两个三元组
    ]
    
    for nums, expected in test_cases:
        result = three_sum(nums)
        # 排序后比较，因为顺序可能不同
        result.sort()
        expected.sort()
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)