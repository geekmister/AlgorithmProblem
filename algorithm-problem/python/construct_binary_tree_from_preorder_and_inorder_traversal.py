"""
从前序与中序遍历序列构造二叉树 (Construct Binary Tree from Preorder and Inorder Traversal)

问题描述：
根据一棵树的前序遍历与中序遍历构造二叉树。

使用场景：
- 树结构的重建
- 算法设计
- 数据结构的操作

算法难度：中等

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 需要存储中序遍历的索引映射

其他信息：
- 前序遍历的第一个元素是根节点
- 中序遍历中根节点左侧的元素是左子树，右侧的元素是右子树
- 可以使用递归的方法，根据前序和中序遍历的特性构建二叉树
"""

from typing import List, Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """
    根据前序遍历和中序遍历构造二叉树
    
    Args:
        preorder: 前序遍历序列
        inorder: 中序遍历序列
    
    Returns:
        构造的二叉树的根节点
    """
    # 处理空序列的情况
    if not preorder or not inorder:
        return None
    
    # 构建中序遍历的索引映射，方便快速查找根节点的位置
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    
    # 前序遍历的第一个元素是根节点
    root_val = preorder[0]
    root = TreeNode(root_val)
    
    # 找到根节点在中序遍历中的位置
    root_idx = inorder_map[root_val]
    
    # 递归构建左右子树
    # 左子树的前序遍历是 preorder[1:1+root_idx]
    # 左子树的中序遍历是 inorder[:root_idx]
    root.left = build_tree(preorder[1:1+root_idx], inorder[:root_idx])
    
    # 右子树的前序遍历是 preorder[1+root_idx:]
    # 右子树的中序遍历是 inorder[root_idx+1:]
    root.right = build_tree(preorder[1+root_idx:], inorder[root_idx+1:])
    
    return root


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    前序遍历二叉树
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        前序遍历的节点值列表
    """
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
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
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]),  # 标准测试用例
        ([1, 2], [2, 1]),  # 只有两个节点
        ([1], [1]),  # 只有一个节点
        ([1, 2, 3], [3, 2, 1])  # 右斜树
    ]
    
    for preorder, inorder in test_cases:
        root = build_tree(preorder, inorder)
        # 验证前序遍历
        result_preorder = preorder_traversal(root)
        # 验证中序遍历
        result_inorder = inorder_traversal(root)
        print(f"Input: preorder = {preorder}, inorder = {inorder}")
        print(f"Expected Preorder: {preorder}")
        print(f"Result Preorder: {result_preorder}")
        print(f"Expected Inorder: {inorder}")
        print(f"Result Inorder: {result_inorder}")
        print(f"Pass: {result_preorder == preorder and result_inorder == inorder}")
        print("-" * 50)