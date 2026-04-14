"""
找树左下角的值 (Find Bottom Left Tree Value)

问题描述：
给定一个二叉树，在树的最后一行找到最左边的值。

使用场景：
- 树结构的遍历
- 算法设计
- 数据结构的操作

算法难度：中等

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 需要使用队列来存储节点

其他信息：
- 可以使用层序遍历，记录每一层的第一个节点的值
- 最后一层的第一个节点就是树左下角的值
- 需要考虑空树的情况
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_bottom_left_value(root: Optional[TreeNode]) -> int:
    """
    找到二叉树最后一行最左边的值
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        最后一行最左边的值
    """
    # 处理空树的情况
    if not root:
        return 0
    
    # 初始化队列和结果
    queue = [root]
    bottom_left = root.val
    
    # 层序遍历
    while queue:
        # 记录当前层的节点数
        level_size = len(queue)
        
        # 遍历当前层的所有节点
        for i in range(level_size):
            # 取出队首节点
            node = queue.pop(0)
            
            # 记录当前层的第一个节点的值
            if i == 0:
                bottom_left = node.val
            
            # 将左右子节点加入队列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return bottom_left


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
        ([2, 1, 3], 1),  # 最后一行最左边的值是1
        ([1, 2, 3, 4, None, 5, 6, None, None, 7], 7),  # 最后一行最左边的值是7
        ([1], 1),  # 只有根节点
        ([1, 2], 2)  # 最后一行最左边的值是2
    ]
    
    for values, expected in test_cases:
        root = build_tree(values)
        result = find_bottom_left_value(root)
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)