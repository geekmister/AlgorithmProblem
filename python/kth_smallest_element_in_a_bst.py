"""
二叉搜索树的第K小元素 (Kth Smallest Element in a BST)

问题描述：
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

使用场景：
- 树结构的分析
- 算法设计
- 数据结构的操作

算法难度：中等

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 二叉搜索树的中序遍历是一个升序序列
- 可以利用中序遍历的特性，找到第k个元素
- 需要记录遍历的位置
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    """
    查找二叉搜索树中第k个最小的元素
    
    Args:
        root: 二叉搜索树的根节点
        k: 第k小的元素
    
    Returns:
        第k小的元素的值
    """
    # 初始化计数器和结果
    count = 0
    result = 0
    
    # 中序遍历
    def inorder(node):
        nonlocal count, result
        
        if not node:
            return
        
        # 遍历左子树
        inorder(node.left)
        
        # 增加计数器
        count += 1
        # 当计数器等于k时，记录结果
        if count == k:
            result = node.val
            return
        
        # 遍历右子树
        inorder(node.right)
    
    # 调用中序遍历
    inorder(root)
    
    return result


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


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([3, 1, 4, None, 2], 1, 1),  # 第1小的元素是1
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3),  # 第3小的元素是3
        ([1], 1, 1),  # 只有根节点
        ([2, 1, 3], 2, 2)  # 第2小的元素是2
    ]
    
    for values, k, expected in test_cases:
        root = build_tree(values)
        result = kth_smallest(root, k)
        print(f"Input: values = {values}, k = {k}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)