"""
二叉树的层序遍历 (Binary Tree Level Order Traversal)

问题描述：
给你一个二叉树，请你返回其按层序遍历得到的节点值。 （即逐层地，从左到右访问所有节点）。

使用场景：
- 树结构的遍历
- 算法设计
- 数据结构的操作

算法难度：中等

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 需要使用队列来存储节点

其他信息：
- 层序遍历是一种广度优先搜索（BFS）
- 使用队列来实现层序遍历
- 需要记录每一层的节点数
"""

from typing import List

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode) -> List[List[int]]:
    """
    二叉树的层序遍历
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        按层序遍历得到的节点值列表
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
        # 存储当前层的节点值
        level = []
        
        # 遍历当前层的所有节点
        for _ in range(level_size):
            # 取出队首节点
            node = queue.pop(0)
            # 将节点值添加到当前层
            level.append(node.val)
            # 将左右子节点加入队列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # 将当前层添加到结果中
        result.append(level)
    
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
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
        ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),
        ([1, None, 2, None, 3], [[1], [2], [3]])
    ]
    
    for values, expected in test_cases:
        root = build_tree(values)
        result = level_order(root)
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)