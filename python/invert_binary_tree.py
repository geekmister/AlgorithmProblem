"""
翻转二叉树 (Invert Binary Tree)

问题描述：
翻转一棵二叉树。

使用场景：
- 树结构的操作
- 算法设计
- 数据结构的操作

算法难度：简单

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 翻转二叉树是指将每个节点的左右子树交换
- 可以使用深度优先搜索（DFS）递归地翻转二叉树
- 需要考虑空树的情况
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    翻转二叉树
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        翻转后的二叉树的根节点
    """
    # 处理空树的情况
    if not root:
        return None
    
    # 交换左右子树
    root.left, root.right = root.right, root.left
    
    # 递归翻转左右子树
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root


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


def level_order(root: Optional[TreeNode]) -> list:
    """
    层序遍历二叉树
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        层序遍历的节点值列表
    """
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([4, 2, 7, 1, 3, 6, 9], [[4], [7, 2], [9, 6, 3, 1]]),  # 翻转后的层序遍历
        ([2, 1, 3], [[2], [3, 1]]),  # 翻转后的层序遍历
        ([], []),  # 空树
        ([1], [[1]])  # 只有根节点
    ]
    
    for values, expected in test_cases:
        root = build_tree(values)
        inverted_root = invert_tree(root)
        result = level_order(inverted_root)
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)