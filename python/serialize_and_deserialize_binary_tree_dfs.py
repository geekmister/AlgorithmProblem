"""
二叉树的序列化与反序列化（DFS版本） (Serialize and Deserialize Binary Tree using DFS)

问题描述：
设计一个算法，使用深度优先搜索（DFS）将二叉树序列化为字符串，然后将字符串反序列化为二叉树。

使用场景：
- 树结构的存储和传输
- 数据结构的操作
- 算法设计

算法难度：困难

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 递归调用栈的深度

其他信息：
- 可以使用前序遍历（根-左-右）来序列化和反序列化二叉树
- 序列化时，使用特殊字符表示空节点
- 反序列化时，按照前序遍历的顺序构建二叉树
"""

from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        使用前序遍历将二叉树序列化为字符串
        
        Args:
            root: 二叉树的根节点
        
        Returns:
            序列化后的字符串
        """
        # 递归函数
        def dfs(node):
            if not node:
                return "null,"
            # 前序遍历：根-左-右
            return str(node.val) + "," + dfs(node.left) + dfs(node.right)
        
        return dfs(root)
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        将字符串反序列化为二叉树
        
        Args:
            data: 序列化后的字符串
        
        Returns:
            反序列化后的二叉树的根节点
        """
        # 分割字符串并去除末尾的逗号
        values = data.split(",")[:-1]
        # 指针，记录当前处理的位置
        self.index = 0
        
        # 递归函数
        def dfs():
            if values[self.index] == "null":
                self.index += 1
                return None
            # 创建当前节点
            node = TreeNode(int(values[self.index]))
            self.index += 1
            # 构建左子树和右子树
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()


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


def preorder_traversal(root: Optional[TreeNode]) -> list:
    """
    前序遍历二叉树
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        前序遍历的节点值列表
    """
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        [1, 2, 3, None, None, 4, 5],  # 标准测试用例
        [],  # 空树
        [1],  # 只有根节点
        [1, 2]  # 只有根节点和左子节点
    ]
    
    codec = Codec()
    
    for values in test_cases:
        root = build_tree(values)
        serialized = codec.serialize(root)
        deserialized = codec.deserialize(serialized)
        result = preorder_traversal(deserialized)
        expected = preorder_traversal(root)
        print(f"Input: {values}")
        print(f"Serialized: {serialized}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)