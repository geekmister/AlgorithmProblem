"""
二叉树的层序遍历 II (Binary Tree Level Order Traversal II)

问题描述：
给定一个二叉树，返回其节点值自底向上的层序遍历。

使用场景：
- 树结构的遍历
- 算法设计
- 数据结构的操作

算法难度：中等

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 需要使用队列来存储节点

其他信息：
- 自底向上的层序遍历是指从叶子节点所在的层到根节点所在的层，逐层遍历
- 可以使用标准的层序遍历，然后将结果反转
- 需要考虑空树的情况
"""

from typing import List, Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_bottom(root: Optional[TreeNode]) -> List[List[int]]:
    """
    返回二叉树自底向上的层序遍历
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        自底向上的层序遍历结果
    """
    # 处理空树的情况
    if not root:
        return []
    
    # 初始化结果列表和队列
    result = []
    queue = [root]
    
    # 层序遍历
    while queue:
        # 记录当前层的节点数
        level_size = len(queue)
        level = []
        
        # 遍历当前层的所有节点
        for _ in range(level_size):
            # 取出队首节点
            node = queue.pop(0)
            # 添加节点值到当前层
            level.append(node.val)
            # 将左右子节点加入队列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # 将当前层添加到结果的开头
        result.insert(0, level)
    
    return result


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
        ([3, 9, 20, None, None, 15, 7], [[15, 7], [9, 20], [3]]),  # 自底向上的层序遍历
        ([1], [[1]]),  # 只有根节点
        ([], []),  # 空树
        ([1, 2, 3, 4, 5, 6, 7], [[4, 5, 6, 7], [2, 3], [1]])  # 自底向上的层序遍历
    ]
    
    for values, expected in test_cases:
        root = build_tree(values)
        result = level_order_bottom(root)
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)