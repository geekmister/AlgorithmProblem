"""
组合总和 II (Combination Sum II)

问题描述：
给定一个数组 candidates 和一个目标数 target，找出 candidates 中所有可以使数字和为 target 的组合。

使用场景：
- 数组操作
- 算法设计
- 回溯算法

算法难度：中等

时间复杂度：O(2^n) - n是数组的长度
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- candidates 中的每个数字在每个组合中只能使用一次
- 解集不能包含重复的组合
- 可以使用回溯算法，遍历所有可能的组合
- 需要处理重复元素的情况
"""

from typing import List


def combination_sum_ii(candidates: List[int], target: int) -> List[List[int]]:
    """
    找出所有可以使数字和为target的组合
    
    Args:
        candidates: 可能包含重复元素的数组
        target: 目标数
    
    Returns:
        所有可以使数字和为target的组合
    """
    result = []
    
    # 对数组进行排序，方便剪枝和处理重复元素
    candidates.sort()
    
    # 回溯函数
    def backtrack(start, current, current_sum):
        # 如果当前和等于目标值，将当前组合添加到结果中
        if current_sum == target:
            result.append(current.copy())
            return
        
        # 遍历数组中的元素
        for i in range(start, len(candidates)):
            # 处理重复元素，避免生成重复的组合
            if i > start and candidates[i] == candidates[i-1]:
                continue
            
            # 如果当前元素大于目标值减去当前和，剪枝
            if candidates[i] > target - current_sum:
                break
            
            # 添加当前元素到组合中
            current.append(candidates[i])
            # 递归处理，不允许重复使用当前元素
            backtrack(i + 1, current, current_sum + candidates[i])
            # 回溯，移除当前元素
            current.pop()
    
    # 开始回溯
    backtrack(0, [], 0)
    
    return result


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),  # 四个组合
        ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),  # 两个组合
        ([1], 1, [[1]]),  # 一个组合
        ([1], 2, []),  # 没有组合
        ([2, 3, 5], 8, [[3, 5]])  # 一个组合
    ]
    
    for candidates, target, expected in test_cases:
        result = combination_sum_ii(candidates, target)
        # 排序后比较，因为顺序可能不同
        for combo in result:
            combo.sort()
        result.sort()
        for combo in expected:
            combo.sort()
        expected.sort()
        print(f"Input: candidates={candidates}, target={target}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)