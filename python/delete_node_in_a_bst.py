"""
删除二叉搜索树中的节点 (Delete Node in a BST)

问题描述：
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。

使用场景：
- 树结构的操作
- 算法设计
- 数据结构的操作

算法难度：中等

时间复杂度：O(h) - h是树的高度
空间复杂度：O(h) - 递归调用栈的深度

其他信息：
- 二叉搜索树的性质：左子树的所有节点值小于根节点值，右子树的所有节点值大于根节点值
- 删除节点的三种情况：
  1. 节点是叶子节点：直接删除
  2. 节点有一个子节点：用子节点替换该节点
  3. 节点有两个子节点：找到右子树中的最小节点，替换该节点，然后删除右子树中的最小节点
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def delete_node(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    """
    删除二叉搜索树中的节点
    
    Args:
        root: 二叉搜索树的根节点
        key: 要删除的节点值
    
    Returns:
        删除后的二叉搜索树的根节点
    """
    # 处理空树的情况
    if not root:
        return None
    
    # 如果要删除的节点值小于当前节点的值，在左子树中删除
    if key < root.val:
        root.left = delete_node(root.left, key)
    # 如果要删除的节点值大于当前节点的值，在右子树中删除
    elif key > root.val:
        root.right = delete_node(root.right, key)
    # 找到要删除的节点
    else:
        # 情况1：节点是叶子节点
        if not root.left and not root.right:
            return None
        # 情况2：节点有一个子节点
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        # 情况3：节点有两个子节点
        else:
            # 找到右子树中的最小节点
            min_node = find_min(root.right)
            # 用最小节点的值替换当前节点的值
            root.val = min_node.val
            # 删除右子树中的最小节点
            root.right = delete_node(root.right, min_node.val)
    
    # 返回根节点
    return root

def find_min(node: TreeNode) -> TreeNode:
    """
    找到二叉搜索树中的最小节点
    
    Args:
        node: 二叉搜索树的根节点
    
    Returns:
        最小节点
    """
    while node.left:
        node = node.left
    return node

def build_tree(values):
    """
    根据列表构建二叉搜索树
    
    Args:
        values: 包含节点值的列表
    
    Returns:
        二叉搜索树的根节点
    """
    if not values:
        return None
    
    root = TreeNode(values[0])
    for val in values[1:]:
        root = insert_into_bst(root, val)
    
    return root

def insert_into_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    在二叉搜索树中插入新节点
    
    Args:
        root: 二叉搜索树的根节点
        val: 要插入的值
    
    Returns:
        插入后的二叉搜索树的根节点
    """
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    
    return root

def inorder_traversal(root: Optional[TreeNode]) -> list:
    """
    中序遍历二叉树
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        中序遍历的节点值列表
    """
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        # 树结构: 5,3,6,2,4,null,7
        # 删除3 → 中序遍历应该是 [2,4,5,6,7]
        ([5, 3, 6, 2, 4, None, 7], 3, [2, 4, 5, 6, 7]),
        # 树结构: 5,3,6,2,4,null,7
        # 删除5 → 中序遍历应该是 [2,3,4,6,7]
        ([5, 3, 6, 2, 4, None, 7], 5, [2, 3, 4, 6, 7]),
        # 空树，删除1 → 中序遍历应该是 []
        ([], 1, []),
        # 树结构: 1
        # 删除1 → 中序遍历应该是 []
        ([1], 1, [])
    ]
    
    for values, key, expected in test_cases:
        root = build_tree(values)
        new_root = delete_node(root, key)
        result = inorder_traversal(new_root)
        print(f"Input: values={values}, key={key}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)