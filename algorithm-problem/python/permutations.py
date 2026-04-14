"""
全排列 (Permutations)

问题描述：
给定一个不含重复数字的数组 nums，返回其所有可能的全排列。

使用场景：
- 数组操作
- 算法设计
- 回溯算法

算法难度：中等

时间复杂度：O(n!) - n是数组的长度
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 全排列是指将数组中的所有元素排列成不同的顺序
- 可以使用回溯算法，遍历所有可能的排列
- 需要记录已经使用过的元素
"""

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    """
    生成所有可能的全排列
    
    Args:
        nums: 不含重复数字的数组
    
    Returns:
        所有可能的全排列
    """
    result = []
    n = len(nums)
    
    # 回溯函数
    def backtrack(current, used):
        # 如果当前排列的长度等于数组的长度，将当前排列添加到结果中
        if len(current) == n:
            result.append(current.copy())
            return
        
        # 遍历数组中的元素
        for i in range(n):
            # 如果元素已经使用过，跳过
            if used[i]:
                continue
            
            # 标记元素为已使用
            used[i] = True
            # 添加元素到当前排列中
            current.append(nums[i])
            # 递归处理
            backtrack(current, used)
            # 回溯，标记元素为未使用
            used[i] = False
            # 移除元素
            current.pop()
    
    # 开始回溯
    backtrack([], [False] * n)
    
    return result


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),  # 6个排列
        ([0, 1], [[0, 1], [1, 0]]),  # 2个排列
        ([1], [[1]]),  # 1个排列
    ]
    
    for nums, expected in test_cases:
        result = permute(nums)
        # 排序后比较，因为顺序可能不同
        result.sort()
        expected.sort()
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)