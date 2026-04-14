"""
二叉搜索树中的众数 (Find Mode in Binary Search Tree)

问题描述：
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

使用场景：
- 树结构的分析
- 算法设计
- 数据结构的操作

算法难度：简单

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(1) - 只使用常数级别的额外空间（不包括返回的结果）

其他信息：
- 二叉搜索树的中序遍历是一个升序序列
- 可以利用中序遍历的特性，统计每个元素的出现次数
- 需要记录当前元素的出现次数、最大出现次数和众数列表
"""

from typing import List, Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_mode(root: Optional[TreeNode]) -> List[int]:
    """
    找出二叉搜索树中的所有众数
    
    Args:
        root: 二叉搜索树的根节点
    
    Returns:
        众数列表
    """
    # 初始化变量
    current_val = None
    current_count = 0
    max_count = 0
    modes = []
    
    # 中序遍历
    def inorder(node):
        nonlocal current_val, current_count, max_count, modes
        
        if node:
            # 遍历左子树
            inorder(node.left)
            
            # 处理当前节点
            if node.val == current_val:
                current_count += 1
            else:
                current_val = node.val
                current_count = 1
            
            # 更新众数列表
            if current_count > max_count:
                max_count = current_count
                modes = [current_val]
            elif current_count == max_count:
                modes.append(current_val)
            
            # 遍历右子树
            inorder(node.right)
    
    # 调用中序遍历
    inorder(root)
    
    return modes


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


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([1, None, 2, 2], [2]),  # 众数是2
        ([0], [0]),  # 只有一个节点
        ([1, 2, 2, 3, 3, 3], [3]),  # 众数是3
        ([1, 1, 2, 2, 3], [1, 2])  # 众数是1和2
    ]
    
    for values, expected in test_cases:
        root = build_tree(values)
        result = find_mode(root)
        # 排序后比较，因为顺序可能不同
        result.sort()
        expected.sort()
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)