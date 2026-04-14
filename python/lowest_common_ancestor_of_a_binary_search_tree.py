"""
二叉搜索树的最近公共祖先 (Lowest Common Ancestor of a Binary Search Tree)

问题描述：
给定一个二叉搜索树，找到该树中两个指定节点的最近公共祖先。

使用场景：
- 树结构的分析
- 算法设计
- 数据结构的操作

算法难度：简单

时间复杂度：O(h) - h是树的高度
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 二叉搜索树的性质：左子树的所有节点值小于根节点值，右子树的所有节点值大于根节点值
- 可以利用二叉搜索树的性质，通过比较节点值来找到最近公共祖先
- 如果两个节点的值都小于当前节点的值，那么最近公共祖先在左子树中
- 如果两个节点的值都大于当前节点的值，那么最近公共祖先在右子树中
- 否则，当前节点就是最近公共祖先
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
    找到二叉搜索树中两个指定节点的最近公共祖先
    
    Args:
        root: 二叉搜索树的根节点
        p: 第一个指定节点
        q: 第二个指定节点
    
    Returns:
        最近公共祖先
    """
    # 处理空树的情况
    if not root:
        return None
    
    # 如果两个节点的值都小于当前节点的值，那么最近公共祖先在左子树中
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    
    # 如果两个节点的值都大于当前节点的值，那么最近公共祖先在右子树中
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    
    # 否则，当前节点就是最近公共祖先
    return root


def build_tree(values):
    """
    根据列表构建二叉搜索树
    
    Args:
        values: 包含节点值的列表
    
    Returns:
        二叉搜索树的根节点
    """
    if not values:
        return None
    
    root = TreeNode(values[0])
    for val in values[1:]:
        root = insert_into_bst(root, val)
    
    return root

def insert_into_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    在二叉搜索树中插入新节点
    
    Args:
        root: 二叉搜索树的根节点
        val: 要插入的值
    
    Returns:
        插入后的二叉搜索树的根节点
    """
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    
    return root

def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    在二叉搜索树中查找指定值的节点
    
    Args:
        root: 二叉搜索树的根节点
        val: 要查找的节点值
    
    Returns:
        找到的节点，如果不存在则返回None
    """
    if not root:
        return None
    
    if root.val == val:
        return root
    
    if val < root.val:
        return find_node(root.left, val)
    else:
        return find_node(root.right, val)


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        # 树结构: 6,2,8,0,4,7,9,null,null,3,5
        # p=2, q=8 → LCA=6
        # p=2, q=4 → LCA=2
        # p=8, q=9 → LCA=8
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 8, 9, 8),
        # 树结构: 2,1
        # p=2, q=1 → LCA=2
        ([2, 1], 2, 1, 2)
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