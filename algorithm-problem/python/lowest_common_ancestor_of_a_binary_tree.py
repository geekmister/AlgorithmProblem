"""
二叉树的最近公共祖先 (Lowest Common Ancestor of a Binary Tree)

问题描述：
给定一个二叉树，找到该树中两个指定节点的最近公共祖先。

使用场景：
- 树结构的分析
- 算法设计
- 数据结构的操作

算法难度：中等

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 最近公共祖先（LCA）是指两个节点的公共祖先中离它们最近的那个
- 可以使用深度优先搜索（DFS），递归地查找左右子树
- 如果一个节点是另一个节点的祖先，那么它就是最近公共祖先
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    找到二叉树中两个指定节点的最近公共祖先
    
    Args:
        root: 二叉树的根节点
        p: 第一个指定节点
        q: 第二个指定节点
    
    Returns:
        最近公共祖先
    """
    # 处理空树的情况
    if not root:
        return None
    
    # 如果当前节点是p或q，直接返回当前节点
    if root == p or root == q:
        return root
    
    # 递归查找左右子树
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    # 如果左右子树都找到了节点，说明当前节点是最近公共祖先
    if left and right:
        return root
    
    # 如果只有左子树找到了节点，返回左子树的结果
    if left:
        return left
    
    # 如果只有右子树找到了节点，返回右子树的结果
    return right


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

def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    在二叉树中查找指定值的节点
    
    Args:
        root: 二叉树的根节点
        val: 要查找的节点值
    
    Returns:
        找到的节点，如果不存在则返回None
    """
    if not root:
        return None
    
    if root.val == val:
        return root
    
    left = find_node(root.left, val)
    if left:
        return left
    
    return find_node(root.right, val)


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        # 树结构: 3,9,20,null,null,15,7
        # p=9, q=20 → LCA=3
        # p=9, q=15 → LCA=3
        # p=15, q=7 → LCA=20
        ([3, 9, 20, None, None, 15, 7], 9, 20, 3),
        ([3, 9, 20, None, None, 15, 7], 9, 15, 3),
        ([3, 9, 20, None, None, 15, 7], 15, 7, 20),
        # 树结构: 1,2
        # p=1, q=2 → LCA=1
        ([1, 2], 1, 2, 1)
    ]
    
    for values, p_val, q_val, expected_val in test_cases:
        root = build_tree(values)
        p = find_node(root, p_val)
        q = find_node(root, q_val)
        lca = lowest_common_ancestor(root, p, q)
        result = lca.val if lca else None
        print(f"Input: values={values}, p={p_val}, q={q_val}")
        print(f"Expected: {expected_val}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected_val}")
        print("-" * 50)