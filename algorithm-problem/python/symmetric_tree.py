"""
对称二叉树 (Symmetric Tree)

问题描述：
给定一个二叉树，检查它是否是镜像对称的。

使用场景：
- 树结构的分析
- 数据结构的验证
- 算法设计

算法难度：简单

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 可以使用递归或迭代的方法
- 递归方法更直观，通过比较左右子树是否对称
- 需要考虑空树的情况（空树是对称的）
"""

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: TreeNode) -> bool:
    """
    检查二叉树是否是镜像对称的
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        是否是镜像对称的
    """
    # 辅助函数，检查两个子树是否对称
    def is_mirror(left: TreeNode, right: TreeNode) -> bool:
        # 两个子树都为空，对称
        if not left and not right:
            return True
        # 只有一个子树为空，不对称
        if not left or not right:
            return False
        # 检查当前节点的值是否相等，以及左右子树是否对称
        return (left.val == right.val) and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
    
    # 处理空树的情况
    if not root:
        return True
    
    # 检查左右子树是否对称
    return is_mirror(root.left, root.right)


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
        ([1, 2, 2, 3, 4, 4, 3], True),  # 对称二叉树
        ([1, 2, 2, None, 3, None, 3], False),  # 不对称二叉树
        ([], True),  # 空树
        ([1], True),  # 只有根节点
        ([1, 2, 3], False)  # 不对称二叉树
    ]
    
    for values, expected in test_cases:
        root = build_tree(values)
        result = is_symmetric(root)
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)