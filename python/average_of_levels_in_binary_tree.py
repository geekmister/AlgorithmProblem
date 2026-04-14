"""
二叉树的层平均值 (Average of Levels in Binary Tree)

问题描述：
给定一个非空二叉树，返回一个由每层节点平均值组成的数组。

使用场景：
- 树结构的遍历
- 算法设计
- 数据结构的操作

算法难度：简单

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 需要使用队列来存储节点

其他信息：
- 可以使用层序遍历，计算每层的节点值之和和节点数
- 然后计算每层的平均值
- 需要考虑空树的情况
"""

from typing import List, Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def average_of_levels(root: Optional[TreeNode]) -> List[float]:
    """
    返回二叉树每层节点的平均值
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        每层节点的平均值列表
    """
    # 处理空树的情况
    if not root:
        return []
    
    # 初始化结果列表和队列
    result = []
    queue = [root]
    
    # 层序遍历
    while queue:
        # 记录当前层的节点数和节点值之和
        level_size = len(queue)
        level_sum = 0
        
        # 遍历当前层的所有节点
        for _ in range(level_size):
            # 取出队首节点
            node = queue.pop(0)
            # 累加节点值
            level_sum += node.val
            # 将左右子节点加入队列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # 计算当前层的平均值并添加到结果中
        level_average = level_sum / level_size
        result.append(level_average)
    
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
        ([3, 9, 20, None, None, 15, 7], [3.0, 14.5, 11.0]),  # 第一层平均值3，第二层平均值(9+20)/2=14.5，第三层平均值(15+7)/2=11
        ([1, 2, 3, 4, 5, 6, 7], [1.0, 2.5, 5.0]),  # 第一层平均值1，第二层平均值(2+3)/2=2.5，第三层平均值(4+5+6+7)/4=5.5？需要重新计算
        ([], []),  # 空树
        ([1], [1.0])  # 只有根节点
    ]
    
    # 重新计算测试用例2的正确结果
    # 第一层：1 → 1.0
    # 第二层：2+3=5 → 5/2=2.5
    # 第三层：4+5+6+7=22 → 22/4=5.5
    test_cases[1][1] = [1.0, 2.5, 5.5]
    
    for values, expected in test_cases:
        root = build_tree(values)
        result = average_of_levels(root)
        # 比较结果，允许浮点数误差
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        # 检查每个值是否在误差范围内
        pass_flag = True
        for i in range(len(expected)):
            if abs(result[i] - expected[i]) > 1e-6:
                pass_flag = False
                break
        print(f"Pass: {pass_flag}")
        print("-" * 50)