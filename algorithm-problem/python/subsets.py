"""
子集 (Subsets)

问题描述：
给定一个整数数组 nums，返回该数组所有可能的子集（幂集）。

使用场景：
- 数组操作
- 算法设计
- 回溯算法

算法难度：中等

时间复杂度：O(2^n) - n是数组的长度
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 幂集是指包含所有可能的子集的集合
- 空集和原数组本身都是子集
- 可以使用回溯算法，遍历所有可能的子集
- 也可以使用位运算，每个元素有选或不选两种状态
"""

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """
    生成所有可能的子集
    
    Args:
        nums: 整数数组
    
    Returns:
        所有可能的子集
    """
    result = []
    n = len(nums)
    
    # 回溯函数
    def backtrack(start, current):
        # 将当前子集添加到结果中
        result.append(current.copy())
        
        # 遍历数组中的元素
        for i in range(start, n):
            # 添加元素到当前子集中
            current.append(nums[i])
            # 递归处理
            backtrack(i + 1, current)
            # 回溯，移除元素
            current.pop()
    
    # 开始回溯
    backtrack(0, [])
    
    return result


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([1, 2, 3], [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]),  # 8个子集
        ([0], [[], [0]]),  # 2个子集
        ([], [[]]),  # 1个子集
    ]
    
    for nums, expected in test_cases:
        result = subsets(nums)
        # 排序后比较，因为顺序可能不同
        for subset in result:
            subset.sort()
        result.sort()
        for subset in expected:
            subset.sort()
        expected.sort()
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)