"""
将有序数组转换为二叉搜索树 (Convert Sorted Array to Binary Search Tree)

问题描述：
给定一个按照升序排列的有序数组，将其转换为一棵高度平衡的二叉搜索树。

使用场景：
- 树结构的构建
- 算法设计
- 数据结构的操作

算法难度：简单

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 高度平衡的二叉搜索树是指每个节点的左右子树的高度差不超过1
- 可以使用二分法，选择数组的中间元素作为根节点，然后递归地构建左右子树
- 这样可以保证树的高度平衡
"""

from typing import List, Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
    """
    将有序数组转换为高度平衡的二叉搜索树
    
    Args:
        nums: 按照升序排列的有序数组
    
    Returns:
        高度平衡的二叉搜索树的根节点
    """
    # 处理空数组的情况
    if not nums:
        return None
    
    # 找到数组的中间元素作为根节点
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    
    # 递归构建左右子树
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])
    
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


def is_balanced(root: Optional[TreeNode]) -> bool:
    """
    判断二叉树是否是高度平衡的
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        是否是高度平衡的
    """
    # 辅助函数，返回子树是否平衡以及子树的高度
    def helper(node):
        if not node:
            return True, 0
        
        left_balanced, left_height = helper(node.left)
        right_balanced, right_height = helper(node.right)
        
        is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        height = max(left_height, right_height) + 1
        
        return is_balanced, height
    
    balanced, _ = helper(root)
    return balanced


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([-10, -3, 0, 5, 9], True),  # 转换为高度平衡的二叉搜索树
        ([1, 3], True),  # 转换为高度平衡的二叉搜索树
        ([], True),  # 空数组
        ([1], True)  # 只有一个元素的数组
    ]
    
    for nums, expected_balanced in test_cases:
        root = sorted_array_to_bst(nums)
        inorder_result = inorder_traversal(root)
        balanced = is_balanced(root)
        print(f"Input: {nums}")
        print(f"Inorder traversal: {inorder_result}")
        print(f"Expected balanced: {expected_balanced}")
        print(f"Result balanced: {balanced}")
        print(f"Pass: {balanced == expected_balanced and inorder_result == nums}")
        print("-" * 50)