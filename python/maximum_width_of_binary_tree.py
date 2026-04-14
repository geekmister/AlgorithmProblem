"""
二叉树的最大宽度 (Maximum Width of Binary Tree)

问题描述：
给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是指每一层中的最大节点数。

使用场景：
- 树结构的分析
- 算法设计
- 数据结构的操作

算法难度：中等

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 需要使用队列来存储节点和它们的位置

其他信息：
- 宽度是指每一层中最左和最右的非空节点之间的节点数
- 可以使用层序遍历（BFS），记录每个节点的位置
- 需要为每个节点分配一个唯一的位置值，以便计算宽度
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def width_of_binary_tree(root: Optional[TreeNode]) -> int:
    """
    获取二叉树的最大宽度
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        二叉树的最大宽度
    """
    # 处理空树的情况
    if not root:
        return 0
    
    # 初始化队列，存储节点和它们的位置
    queue = [(root, 0)]
    max_width = 0
    
    # 层序遍历
    while queue:
        # 记录当前层的节点数和起始位置
        level_size = len(queue)
        start_pos = queue[0][1]
        
        # 遍历当前层的所有节点
        for i in range(level_size):
            node, pos = queue.pop(0)
            
            # 计算当前层的宽度
            if i == level_size - 1:
                current_width = pos - start_pos + 1
                max_width = max(max_width, current_width)
            
            # 将左右子节点加入队列，并分配位置
            if node.left:
                queue.append((node.left, 2 * pos))
            if node.right:
                queue.append((node.right, 2 * pos + 1))
    
    return max_width


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
        ([1, 3, 2, 5, 3, None, 9], 4),  # 最大宽度是4（第三层）
        ([1, 3, 2, 5, None, None, 9, 6, None, 7], 7),  # 最大宽度是7（第四层）
        ([1, 3, 2, 5], 2),  # 最大宽度是2（第二层）
        ([1], 1),  # 只有根节点
        ([1, 2], 1)  # 最大宽度是1（第二层）
    ]
    
    for values, expected in test_cases:
        root = build_tree(values)
        result = width_of_binary_tree(root)
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)