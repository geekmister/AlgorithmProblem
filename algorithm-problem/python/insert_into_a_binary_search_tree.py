"""
二叉搜索树中的插入操作 (Insert into a Binary Search Tree)

问题描述：
给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入到二叉搜索树中。

使用场景：
- 树结构的操作
- 算法设计
- 数据结构的操作

算法难度：中等

时间复杂度：O(h) - h是树的高度
空间复杂度：O(h) - 递归调用栈的深度

其他信息：
- 二叉搜索树的性质：左子树的所有节点值小于根节点值，右子树的所有节点值大于根节点值
- 可以利用二叉搜索树的性质，通过比较节点值来找到插入位置
- 插入操作不会改变原有的二叉搜索树结构
- 新节点总是作为叶子节点插入
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_into_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    在二叉搜索树中插入新节点
    
    Args:
        root: 二叉搜索树的根节点
        val: 要插入的值
    
    Returns:
        插入后的二叉搜索树的根节点
    """
    # 处理空树的情况
    if not root:
        return TreeNode(val)
    
    # 如果要插入的值小于当前节点的值，插入到左子树
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    # 如果要插入的值大于当前节点的值，插入到右子树
    else:
        root.right = insert_into_bst(root.right, val)
    
    # 返回根节点
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

def inorder_traversal(root: Optional[TreeNode]) -> list:
    """
    中序遍历二叉树
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        中序遍历的节点值列表
    """
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        # 树结构: 4,2,7,1,3
        # 插入5 → 中序遍历应该是 [1,2,3,4,5,7]
        ([4, 2, 7, 1, 3], 5, [1, 2, 3, 4, 5, 7]),
        # 空树，插入1 → 中序遍历应该是 [1]
        ([], 1, [1]),
        # 树结构: 1
        # 插入2 → 中序遍历应该是 [1,2]
        ([1], 2, [1, 2]),
        # 树结构: 1
        # 插入0 → 中序遍历应该是 [0,1]
        ([1], 0, [0, 1])
    ]
    
    for values, val, expected in test_cases:
        root = build_tree(values)
        new_root = insert_into_bst(root, val)
        result = inorder_traversal(new_root)
        print(f"Input: values={values}, val={val}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)