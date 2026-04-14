"""
验证二叉搜索树 (Validate Binary Search Tree)

问题描述：
给定一个二叉树，判断它是否是一个有效的二叉搜索树。

使用场景：
- 树结构的验证
- 算法设计
- 数据结构的操作

算法难度：中等

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 二叉搜索树的性质：左子树的所有节点值小于根节点值，右子树的所有节点值大于根节点值
- 可以使用中序遍历，检查遍历结果是否是升序的
- 可以使用递归，为每个节点设置上下界
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """
    判断二叉树是否是有效的二叉搜索树
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        是否是有效的二叉搜索树
    """
    # 辅助函数，为每个节点设置上下界
    def helper(node, lower=float('-inf'), upper=float('inf')):
        # 处理空树的情况
        if not node:
            return True
        
        # 检查当前节点的值是否在上下界之间
        if node.val <= lower or node.val >= upper:
            return False
        
        # 递归检查左右子树
        # 左子树的上界是当前节点的值
        # 右子树的下界是当前节点的值
        return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
    
    # 调用辅助函数
    return helper(root)


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
        ([2, 1, 3], True),  # 有效的二叉搜索树
        ([5, 1, 4, None, None, 3, 6], False),  # 无效的二叉搜索树（4的左子节点3小于5）
        ([], True),  # 空树
        ([1], True),  # 只有根节点
        ([10, 5, 15, None, None, 6, 20], False)  # 无效的二叉搜索树（6小于10）
    ]
    
    for values, expected in test_cases:
        root = build_tree(values)
        result = is_valid_bst(root)
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)