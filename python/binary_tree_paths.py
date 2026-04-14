"""
二叉树的所有路径 (Binary Tree Paths)

问题描述：
给定一个二叉树，返回所有从根节点到叶子节点的路径。

使用场景：
- 树结构的遍历
- 路径查找
- 算法设计

算法难度：简单

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度和存储路径

其他信息：
- 叶子节点是指没有子节点的节点
- 可以使用深度优先搜索（DFS），记录从根节点到当前节点的路径
- 当到达叶子节点时，将路径添加到结果中
"""

from typing import List, Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    """
    返回二叉树中所有从根节点到叶子节点的路径
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        路径列表
    """
    # 处理空树的情况
    if not root:
        return []
    
    # 初始化结果列表
    result = []
    
    # 深度优先搜索
    def dfs(node, path):
        # 添加当前节点到路径
        path.append(str(node.val))
        
        # 处理叶子节点的情况
        if not node.left and not node.right:
            # 将路径转换为字符串并添加到结果中
            result.append('->'.join(path))
        else:
            # 递归遍历左右子树
            if node.left:
                dfs(node.left, path.copy())
            if node.right:
                dfs(node.right, path.copy())
    
    # 调用深度优先搜索
    dfs(root, [])
    
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
        ([1, 2, 3, None, 5], ["1->2->5", "1->3"]),  # 标准测试用例
        ([1], ["1"]),  # 只有根节点
        ([], []),  # 空树
        ([1, 2], ["1->2"])  # 只有根节点和左子节点
    ]
    
    for values, expected in test_cases:
        root = build_tree(values)
        result = binary_tree_paths(root)
        # 排序后比较，因为顺序可能不同
        result.sort()
        expected.sort()
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)