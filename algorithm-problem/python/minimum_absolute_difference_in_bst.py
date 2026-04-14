"""
二叉搜索树的最小绝对差 (Minimum Absolute Difference in BST)

问题描述：
给定一个二叉搜索树的根节点 root，返回树中任意两节点的差的绝对值的最小值。

使用场景：
- 树结构的分析
- 算法设计
- 数据结构的操作

算法难度：简单

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 二叉搜索树的中序遍历是一个升序序列
- 可以利用中序遍历的特性，计算相邻节点的差的绝对值，找到最小值
- 需要记录前一个节点的值
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_minimum_difference(root: Optional[TreeNode]) -> int:
    """
    计算二叉搜索树中任意两节点的差的绝对值的最小值
    
    Args:
        root: 二叉搜索树的根节点
    
    Returns:
        最小绝对差
    """
    # 初始化前一个节点的值和最小差
    prev = None
    min_diff = float('inf')
    
    # 中序遍历
    def inorder(node):
        nonlocal prev, min_diff
        
        if node:
            # 遍历左子树
            inorder(node.left)
            
            # 计算当前节点与前一个节点的差的绝对值
            if prev is not None:
                min_diff = min(min_diff, abs(node.val - prev))
            # 更新前一个节点的值
            prev = node.val
            
            # 遍历右子树
            inorder(node.right)
    
    # 调用中序遍历
    inorder(root)
    
    return min_diff


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
        ([4, 2, 6, 1, 3], 1),  # 最小差是1（2-1或3-2）
        ([1, 0, 48, None, None, 12, 49], 1),  # 最小差是1（48-49）
        ([5, 3, 7, 2, 4, 6, 8], 1),  # 最小差是1
        ([236, 104, 701, None, 227, None, 911], 9)  # 最小差是9（236-227）
    ]
    
    for values, expected in test_cases:
        root = build_tree(values)
        result = get_minimum_difference(root)
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)