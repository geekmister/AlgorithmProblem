"""
验证二叉搜索树的中序遍历 (Validate BST Using Inorder Traversal)

问题描述：
给定一个二叉树，使用中序遍历的方法判断它是否是一个有效的二叉搜索树。

使用场景：
- 树结构的验证
- 算法设计
- 数据结构的操作

算法难度：中等

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 二叉搜索树的中序遍历是一个升序序列
- 可以利用中序遍历的特性，检查遍历结果是否是升序的
- 需要记录前一个节点的值，确保当前节点的值大于前一个节点的值
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
    使用中序遍历的方法验证二叉树是否是有效的二叉搜索树
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        是否是有效的二叉搜索树
    """
    # 初始化前一个节点的值
    prev = None
    
    # 中序遍历
    def inorder(node):
        nonlocal prev
        
        if not node:
            return True
        
        # 遍历左子树
        if not inorder(node.left):
            return False
        
        # 检查当前节点的值是否大于前一个节点的值
        if prev is not None and node.val <= prev:
            return False
        # 更新前一个节点的值
        prev = node.val
        
        # 遍历右子树
        return inorder(node.right)
    
    # 调用中序遍历
    return inorder(root)


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