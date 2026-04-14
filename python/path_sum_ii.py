"""
路径总和 II (Path Sum II)

问题描述：
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

使用场景：
- 树结构的遍历
- 路径查找
- 算法设计

算法难度：中等

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度和存储路径

其他信息：
- 叶子节点是指没有子节点的节点
- 可以使用深度优先搜索（DFS）
- 需要记录路径和当前和
"""

from typing import List, Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
    """
    找到所有从根节点到叶子节点路径总和等于给定目标和的路径
    
    Args:
        root: 二叉树的根节点
        target_sum: 目标和
    
    Returns:
        路径列表
    """
    # 处理空树的情况
    if not root:
        return []
    
    # 初始化结果列表和路径
    result = []
    path = []
    
    # 深度优先搜索
    def dfs(node, current_sum):
        # 添加当前节点到路径
        path.append(node.val)
        current_sum += node.val
        
        # 处理叶子节点的情况
        if not node.left and not node.right:
            if current_sum == target_sum:
                result.append(path.copy())
        else:
            # 递归检查左右子树
            if node.left:
                dfs(node.left, current_sum)
            if node.right:
                dfs(node.right, current_sum)
        
        # 回溯，移除当前节点
        path.pop()
    
    # 调用递归函数
    dfs(root, 0)
    
    return result


def build_tree(values):
    """
    根据列表构建二叉树
    
    Args:
        values: 包含节点值的列表，None表示空节点
    
    Returns:
        二叉树的根节点
    """
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, [[5, 4, 11, 2], [5, 8, 4, 5]]),
        ([1, 2, 3], 5, []),
        ([], 0, []),
        ([1, 2], 1, [])
    ]
    
    for values, target_sum, expected in test_cases:
        root = build_tree(values)
        result = path_sum(root, target_sum)
        print(f"Input: values = {values}, target_sum = {target_sum}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)