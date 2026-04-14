"""
二叉树中的最大路径和 (Binary Tree Maximum Path Sum)

问题描述：
给定一个非空二叉树，返回其最大路径和。

使用场景：
- 树结构的分析
- 路径查找
- 算法设计

算法难度：困难

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 路径是指从树中的任意节点出发，沿父节点-子节点连接，到达任意节点的序列
- 路径中至少包含一个节点，且不一定经过根节点
- 可以使用深度优先搜索（DFS），记录每个节点的最大贡献值
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: Optional[TreeNode]) -> int:
    """
    计算二叉树中的最大路径和
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        最大路径和
    """
    # 初始化最大路径和
    max_sum = float('-inf')
    
    # 深度优先搜索，返回当前节点的最大贡献值
    def dfs(node):
        nonlocal max_sum
        
        # 处理空节点的情况
        if not node:
            return 0
        
        # 递归计算左右子节点的最大贡献值
        left_gain = max(dfs(node.left), 0)  # 负数贡献值可以选择不使用
        right_gain = max(dfs(node.right), 0)  # 负数贡献值可以选择不使用
        
        # 计算当前节点的最大路径和
        current_sum = node.val + left_gain + right_gain
        
        # 更新全局最大路径和
        max_sum = max(max_sum, current_sum)
        
        # 返回当前节点的最大贡献值（只能选择左子树或右子树中的一个）
        return node.val + max(left_gain, right_gain)
    
    # 调用递归函数
    dfs(root)
    
    return max_sum


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
        ([1, 2, 3], 6),  # 路径：2->1->3
        ([-10, 9, 20, None, None, 15, 7], 42),  # 路径：15->20->7
        ([1], 1),
        ([-3], -3),
        ([2, -1, -2], 2)  # 路径：2
    ]
    
    for values, expected in test_cases:
        root = build_tree(values)
        result = max_path_sum(root)
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)