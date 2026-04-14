"""
相同的树 (Same Tree)

问题描述：
给定两个二叉树，编写一个函数来检验它们是否相同。

使用场景：
- 树结构的比较
- 数据结构的操作
- 算法设计

算法难度：简单

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 两个树相同的条件是：它们的结构相同，并且每个对应位置上的节点值也相同
- 可以使用深度优先搜索（DFS）递归地比较两个树
- 需要考虑空树的情况
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    检验两个二叉树是否相同
    
    Args:
        p: 第一个二叉树的根节点
        q: 第二个二叉树的根节点
    
    Returns:
        两个二叉树是否相同
    """
    # 处理空树的情况
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    # 比较当前节点的值
    if p.val != q.val:
        return False
    
    # 递归比较左右子树
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


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
        ([1, 2, 3], [1, 2, 3], True),  # 相同的树
        ([1, 2], [1, None, 2], False),  # 不同的树
        ([1, 2, 1], [1, 1, 2], False),  # 不同的树
        ([], [], True),  # 两个空树
        ([1], [1], True),  # 两个只有根节点的树
        ([1, None, 2], [1, None, 2], True)  # 相同的树
    ]
    
    for values_p, values_q, expected in test_cases:
        p = build_tree(values_p)
        q = build_tree(values_q)
        result = is_same_tree(p, q)
        print(f"Input: p = {values_p}, q = {values_q}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)