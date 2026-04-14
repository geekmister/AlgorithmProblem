"""
路径总和 III (Path Sum III)

问题描述：
给定一个二叉树，它的每个节点都存放着一个整数值。找出路径和等于给定数值的路径总数。

使用场景：
- 树结构的分析
- 路径查找
- 算法设计

算法难度：中等

时间复杂度：O(n^2) - 每个节点都需要作为起点进行一次遍历
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）
- 可以使用深度优先搜索（DFS），对于每个节点，计算从该节点出发的所有路径的和
- 需要考虑负数的情况
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root: Optional[TreeNode], target_sum: int) -> int:
    """
    计算二叉树中路径和等于给定数值的路径总数
    
    Args:
        root: 二叉树的根节点
        target_sum: 目标和
    
    Returns:
        路径总数
    """
    # 辅助函数，计算从当前节点出发的路径和等于目标和的路径数
    def dfs(node, current_sum):
        if not node:
            return 0
        
        # 计算当前路径的和
        current_sum += node.val
        
        # 计算以当前节点为终点的路径数
        count = 1 if current_sum == target_sum else 0
        
        # 递归计算左右子树
        count += dfs(node.left, current_sum)
        count += dfs(node.right, current_sum)
        
        return count
    
    # 处理空树的情况
    if not root:
        return 0
    
    # 以当前节点为起点的路径数
    count = dfs(root, 0)
    
    # 递归计算左右子树
    count += path_sum(root.left, target_sum)
    count += path_sum(root.right, target_sum)
    
    return count


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
        ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3),  # 路径：5->3, 5->2->1, -3->11
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, 3),  # 路径：5->4->11->2, 5->8->4->5, 4->11->7
        ([1], 1, 1),  # 只有根节点
        ([1, 2], 3, 1),  # 路径：1->2
        ([1, 2, 3], 3, 2)  # 路径：1->2, 3
    ]
    
    for values, target_sum, expected in test_cases:
        root = build_tree(values)
        result = path_sum(root, target_sum)
        print(f"Input: values = {values}, target_sum = {target_sum}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)