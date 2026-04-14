"""
另一个树的子树 (Subtree of Another Tree)

问题描述：
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。

使用场景：
- 树结构的比较
- 数据结构的操作
- 算法设计

算法难度：简单

时间复杂度：O(n*m) - n是s的节点数，m是t的节点数
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 一个树的子树是指该树的一个节点加上它的所有后代节点
- 可以使用深度优先搜索（DFS），对于s的每个节点，检查以该节点为根的子树是否与t相同
- 需要先实现判断两个树是否相同的函数
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_subtree(s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
    """
    检验s中是否包含和t具有相同结构和节点值的子树
    
    Args:
        s: 主二叉树的根节点
        t: 子二叉树的根节点
    
    Returns:
        s是否包含t作为子树
    """
    # 处理空树的情况
    if not t:
        return True
    if not s:
        return False
    
    # 检查当前节点为根的子树是否与t相同
    if is_same_tree(s, t):
        return True
    
    # 递归检查左右子树
    return is_subtree(s.left, t) or is_subtree(s.right, t)


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    检验两个二叉树是否相同
    
    Args:
        p: 第一个二叉树的根节点
        q: 第二个二叉树的根节点
    
    Returns:
        两个二叉树是否相同
    """
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
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
        ([3, 4, 5, 1, 2], [4, 1, 2], True),  # t是s的子树
        ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),  # t不是s的子树
        ([1, 2, 3], [2, 3], False),  # t不是s的子树（缺少根节点）
        ([], [], True),  # 两个空树
        ([1], [1], True),  # 两个只有根节点的树
        ([1, None, 2, 3], [2, 3], True)  # t是s的子树
    ]
    
    for values_s, values_t, expected in test_cases:
        s = build_tree(values_s)
        t = build_tree(values_t)
        result = is_subtree(s, t)
        print(f"Input: s = {values_s}, t = {values_t}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)