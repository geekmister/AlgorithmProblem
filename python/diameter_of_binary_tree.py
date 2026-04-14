"""
二叉树的直径 (Diameter of Binary Tree)

问题描述：
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个节点路径长度中的最大值。这条路径可能穿过也可能不穿过根节点。

使用场景：
- 树结构的分析
- 算法设计
- 数据结构的操作

算法难度：简单

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 直径是指树中任意两个节点之间的最长路径的长度
- 路径的长度是路径中边的数量
- 可以使用深度优先搜索（DFS），计算每个节点的左右子树的最大深度之和
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    """
    计算二叉树的直径
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        二叉树的直径
    """
    # 初始化直径
    diameter = 0
    
    # 深度优先搜索，返回当前节点的最大深度
    def dfs(node):
        nonlocal diameter
        
        if not node:
            return 0
        
        # 计算左右子树的最大深度
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)
        
        # 更新直径
        diameter = max(diameter, left_depth + right_depth)
        
        # 返回当前节点的最大深度
        return max(left_depth, right_depth) + 1
    
    # 调用深度优先搜索
    dfs(root)
    
    return diameter


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
        ([1, 2, 3, 4, 5], 3),  # 直径是3（4->2->1->3 或 5->2->1->3）
        ([1, 2], 1),  # 直径是1（2->1）
        ([], 0),  # 空树，直径是0
        ([1], 0)  # 只有根节点，直径是0
    ]
    
    for values, expected in test_cases:
        root = build_tree(values)
        result = diameter_of_binary_tree(root)
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)