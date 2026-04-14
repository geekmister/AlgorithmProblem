"""
二叉树的坡度 (Binary Tree Tilt)

问题描述：
给定一个二叉树，计算整个树的坡度。

使用场景：
- 树结构的分析
- 算法设计
- 数据结构的操作

算法难度：简单

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 一个树的节点的坡度定义是，该节点左子树的节点之和和右子树节点之和的差的绝对值
- 整个树的坡度就是其所有节点的坡度之和
- 可以使用深度优先搜索（DFS），计算每个节点的子树和
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_tilt(root: Optional[TreeNode]) -> int:
    """
    计算二叉树的坡度
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        二叉树的坡度
    """
    # 初始化坡度总和
    tilt_sum = 0
    
    # 深度优先搜索，返回当前节点的子树和
    def dfs(node):
        nonlocal tilt_sum
        
        if not node:
            return 0
        
        # 计算左右子树的和
        left_sum = dfs(node.left)
        right_sum = dfs(node.right)
        
        # 计算当前节点的坡度并添加到总和
        tilt_sum += abs(left_sum - right_sum)
        
        # 返回当前节点的子树和
        return node.val + left_sum + right_sum
    
    # 调用深度优先搜索
    dfs(root)
    
    return tilt_sum


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
        ([1, 2, 3], 1),  # 节点2的坡度是0，节点3的坡度是0，节点1的坡度是|2-3|=1，总和是1
        ([4, 2, 9, 3, 5, None, 7], 15),  # 各节点的坡度：3->0, 5->0, 2->|3-5|=2, 7->0, 9->0, 4->|(2+3+5)-(9+7)|=|10-16|=6，总和是2+6=8？需要重新计算
        ([21, 7, 14, 1, 1, 2, 2, 3, 3], 9)  # 各节点的坡度总和是9
    ]
    
    # 重新计算测试用例2的正确结果
    # 节点3: 0
    # 节点5: 0
    # 节点2: |3-5|=2
    # 节点7: 0
    # 节点9: |0-7|=7
    # 节点4: |(2+3+5)-(9+7)|=|10-16|=6
    # 总和: 2+7+6=15
    
    test_cases[1][1] = 15
    
    for values, expected in test_cases:
        root = build_tree(values)
        result = find_tilt(root)
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)