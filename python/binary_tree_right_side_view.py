"""
二叉树的右视图 (Binary Tree Right Side View)

问题描述：
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

使用场景：
- 树结构的遍历
- 算法设计
- 数据结构的操作

算法难度：中等

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 需要使用队列来存储节点

其他信息：
- 可以使用层序遍历，每次取每层的最后一个节点
- 需要记录每一层的节点数
- 可以使用深度优先搜索（DFS），优先访问右子树
"""

from typing import List, Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    """
    返回二叉树的右视图
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        从右侧所能看到的节点值列表
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
        
        # 遍历当前层的所有节点
        for i in range(level_size):
            # 取出队首节点
            node = queue.pop(0)
            
            # 如果是当前层的最后一个节点，添加到结果中
            if i == level_size - 1:
                result.append(node.val)
            
            # 将左右子节点加入队列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
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
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
        ([1, None, 3], [1, 3]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4], [1, 3, 4])
    ]
    
    for values, expected in test_cases:
        root = build_tree(values)
        result = right_side_view(root)
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)