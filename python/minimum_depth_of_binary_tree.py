"""
二叉树的最小深度 (Minimum Depth of Binary Tree)

问题描述：
给定一个二叉树，找出其最小深度。

使用场景：
- 树结构的分析
- 算法设计
- 数据结构的操作

算法难度：简单

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 最小深度是从根节点到最近叶子节点的最短路径上的节点数量
- 叶子节点是指没有子节点的节点
- 可以使用广度优先搜索（BFS），找到第一个叶子节点时返回当前深度
- 也可以使用深度优先搜索（DFS），递归计算左右子树的最小深度
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root: Optional[TreeNode]) -> int:
    """
    计算二叉树的最小深度
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        二叉树的最小深度
    """
    # 处理空树的情况
    if not root:
        return 0
    
    # 处理叶子节点的情况
    if not root.left and not root.right:
        return 1
    
    # 处理只有左子树的情况
    if not root.left:
        return min_depth(root.right) + 1
    
    # 处理只有右子树的情况
    if not root.right:
        return min_depth(root.left) + 1
    
    # 处理左右子树都有的情况
    return min(min_depth(root.left), min_depth(root.right)) + 1


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
        ([3, 9, 20, None, None, 15, 7], 2),  # 最小深度是2（3→9）
        ([2, None, 3, None, 4, None, 5, None, 6], 5),  # 最小深度是5（2→3→4→5→6）
        ([], 0),  # 空树
        ([1], 1),  # 只有根节点
        ([1, 2], 2)  # 最小深度是2（1→2）
    ]
    
    for values, expected in test_cases:
        root = build_tree(values)
        result = min_depth(root)
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)