"""
路径总和 (Path Sum)

问题描述：
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

使用场景：
- 树结构的遍历
- 路径查找
- 算法设计

算法难度：简单

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 叶子节点是指没有子节点的节点
- 可以使用深度优先搜索（DFS）
- 需要考虑空树的情况
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    """
    判断二叉树中是否存在根节点到叶子节点的路径，路径和等于目标和
    
    Args:
        root: 二叉树的根节点
        target_sum: 目标和
    
    Returns:
        是否存在这样的路径
    """
    # 处理空树的情况
    if not root:
        return False
    
    # 处理叶子节点的情况
    if not root.left and not root.right:
        return root.val == target_sum
    
    # 递归检查左右子树
    return has_path_sum(root.left, target_sum - root.val) or has_path_sum(root.right, target_sum - root.val)


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
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True),  # 5->4->11->2，和为22
        ([1, 2, 3], 5, False),  # 没有路径和为5
        ([], 0, False),  # 空树
        ([1, 2], 1, False)  # 1不是叶子节点
    ]
    
    for values, target_sum, expected in test_cases:
        root = build_tree(values)
        result = has_path_sum(root, target_sum)
        print(f"Input: values = {values}, target_sum = {target_sum}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)