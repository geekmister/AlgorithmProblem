"""
二叉树的最大深度 (Maximum Depth of Binary Tree)

问题描述：
给定一个二叉树，找出其最大深度。

使用场景：
- 树结构的分析
- 算法设计
- 数据结构的操作

算法难度：简单

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 最大深度是从根节点到最远叶子节点的最长路径上的节点数量
- 叶子节点是指没有子节点的节点
- 可以使用深度优先搜索（DFS），递归计算左右子树的最大深度
- 也可以使用广度优先搜索（BFS），记录每层的深度
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    """
    计算二叉树的最大深度
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        二叉树的最大深度
    """
    # 处理空树的情况
    if not root:
        return 0
    
    # 递归计算左右子树的最大深度
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    # 返回较大的深度加1
    return max(left_depth, right_depth) + 1


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
        ([3, 9, 20, None, None, 15, 7], 3),  # 最大深度是3（3→20→7）
        ([1, None, 2], 2),  # 最大深度是2（1→2）
        ([], 0),  # 空树
        ([1], 1),  # 只有根节点
        ([1, 2, 3, 4, 5], 3)  # 最大深度是3（1→2→4 或 1→2→5 或 1→3）
    ]
    
    for values, expected in test_cases:
        root = build_tree(values)
        result = max_depth(root)
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)