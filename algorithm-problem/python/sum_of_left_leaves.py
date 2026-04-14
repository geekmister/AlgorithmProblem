"""
左叶子之和 (Sum of Left Leaves)

问题描述：
计算给定二叉树的所有左叶子之和。

使用场景：
- 树结构的分析
- 算法设计
- 数据结构的操作

算法难度：简单

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 左叶子是指那些是其父节点的左子节点且没有子节点的节点
- 可以使用深度优先搜索（DFS），判断当前节点的左子节点是否是左叶子
- 需要考虑空树的情况
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_of_left_leaves(root: Optional[TreeNode]) -> int:
    """
    计算二叉树的所有左叶子之和
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        左叶子之和
    """
    # 处理空树的情况
    if not root:
        return 0
    
    # 初始化左叶子之和
    left_leaves_sum = 0
    
    # 检查当前节点的左子节点是否是左叶子
    if root.left and not root.left.left and not root.left.right:
        left_leaves_sum += root.left.val
    
    # 递归计算左右子树的左叶子之和
    left_leaves_sum += sum_of_left_leaves(root.left)
    left_leaves_sum += sum_of_left_leaves(root.right)
    
    return left_leaves_sum


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
        ([3, 9, 20, None, None, 15, 7], 24),  # 左叶子是9和15，和为24
        ([1], 0),  # 没有左叶子
        ([0, 1, 2, 3, 4, 5, 6], 9),  # 左叶子是3和6，和为9
        ([1, 2, 3, 4, 5], 4)  # 左叶子是4
    ]
    
    for values, expected in test_cases:
        root = build_tree(values)
        result = sum_of_left_leaves(root)
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)