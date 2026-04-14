"""
二叉树的序列化与反序列化 (Serialize and Deserialize Binary Tree)

问题描述：
设计一个算法，将二叉树序列化为字符串，然后将字符串反序列化为二叉树。

使用场景：
- 树结构的存储和传输
- 数据结构的操作
- 算法设计

算法难度：困难

时间复杂度：O(n) - 每个节点只访问一次
空间复杂度：O(n) - 需要使用队列来存储节点

其他信息：
- 序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输
- 反序列化是将这些位转换回原始数据结构或对象的过程
- 可以使用层序遍历（BFS）来序列化和反序列化二叉树
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
        将二叉树序列化为字符串
        
        Args:
            root: 二叉树的根节点
        
        Returns:
            序列化后的字符串
        """
        if not root:
            return ""
        
        # 使用层序遍历
        queue = [root]
        result = []
        
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        
        return ",".join(result)
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        将字符串反序列化为二叉树
        
        Args:
            data: 序列化后的字符串
        
        Returns:
            反序列化后的二叉树的根节点
        """
        if not data:
            return None
        
        # 分割字符串
        values = data.split(",")
        
        # 创建根节点
        root = TreeNode(int(values[0]))
        queue = [root]
        i = 1
        
        # 层序遍历构建二叉树
        while queue and i < len(values):
            node = queue.pop(0)
            
            # 处理左子节点
            if values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            
            # 处理右子节点
            if i < len(values) and values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
        
        return root


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


def level_order(root: Optional[TreeNode]) -> list:
    """
    层序遍历二叉树
    
    Args:
        root: 二叉树的根节点
    
    Returns:
        层序遍历的节点值列表
    """
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result


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
        result = level_order(deserialized)
        expected = level_order(root)
        print(f"Input: {values}")
        print(f"Serialized: {serialized}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)