"""
二叉树的前序遍历 (Binary Tree Preorder Traversal)

问题描述：
给定一个二叉树的根节点 root ，返回它的前序遍历。

使用场景：
- 树结构的遍历
- 算法设计
- 数据结构的操作

算法难度：简单

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 前序遍历的顺序是：根节点 -> 左子树 -> 右子树
- 可以使用递归或迭代的方法
- 前序遍历常用于复制树结构
"""

from typing import List, Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    二叉树的前序遍历
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        前序遍历的节点值列表
    """
    # 处理空树的情况
    if not root:
        return []
    
    # 初始化结果列表
    result = []
    
    # 递归前序遍历
    def preorder(node):
        if node:
            # 访问根节点
            result.append(node.val)
            # 遍历左子树
            preorder(node.left)
            # 遍历右子树
            preorder(node.right)
    
    # 调用递归函数
    preorder(root)
    
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
        ([1, None, 2, 3], [1, 2, 3]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 4, 5, 3, 6, 7]),
        ([1, 2, None, 3], [1, 2, 3])
    ]
    
    for values, expected in test_cases:
        root = build_tree(values)
        result = preorder_traversal(root)
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)