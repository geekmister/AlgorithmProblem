"""
平衡二叉树 (Balanced Binary Tree)

问题描述：
给定一个二叉树，判断它是否是高度平衡的。

使用场景：
- 树结构的分析
- 数据结构的操作
- 算法设计

算法难度：简单

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 高度平衡的二叉树是指每个节点的左右子树的高度差不超过1
- 可以使用深度优先搜索（DFS），计算每个节点的左右子树的高度，并检查高度差
- 需要返回两个信息：子树是否平衡，以及子树的高度
"""

from typing import Optional, Tuple

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: Optional[TreeNode]) -> bool:
    """
    判断二叉树是否是高度平衡的
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        是否是高度平衡的
    """
    # 辅助函数，返回子树是否平衡以及子树的高度
    def check_balance(node) -> Tuple[bool, int]:
        # 处理空树的情况
        if not node:
            return True, 0
        
        # 检查左右子树
        left_balanced, left_height = check_balance(node.left)
        right_balanced, right_height = check_balance(node.right)
        
        # 计算当前节点的高度
        current_height = max(left_height, right_height) + 1
        
        # 检查当前节点是否平衡
        is_current_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        
        return is_current_balanced, current_height
    
    # 调用辅助函数
    balanced, _ = check_balance(root)
    return balanced


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
        ([3, 9, 20, None, None, 15, 7], True),  # 平衡二叉树
        ([1, 2, 2, 3, 3, None, None, 4, 4], False),  # 不平衡二叉树
        ([], True),  # 空树
        ([1], True),  # 只有根节点
        ([1, 2, 3], True)  # 平衡二叉树
    ]
    
    for values, expected in test_cases:
        root = build_tree(values)
        result = is_balanced(root)
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)