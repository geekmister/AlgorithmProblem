"""
翻转链表 (Reverse Linked List)

问题描述：
反转一个单链表。

使用场景：
- 链表操作
- 数据结构的转换
- 算法设计

算法难度：简单

时间复杂度：O(n) - 只需遍历链表一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 可以使用迭代或递归的方法
- 迭代方法更高效，因为避免了递归调用的开销
- 需要注意链表为空或只有一个节点的情况
"""

# 定义链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    """
    反转单链表
    
    Args:
        head: 链表的头节点
    
    Returns:
        反转后的链表头节点
    """
    # 处理空链表或只有一个节点的情况
    if not head or not head.next:
        return head
    
    # 初始化三个指针
    prev = None
    current = head
    
    # 遍历链表，逐个反转节点
    while current:
        # 保存下一个节点
        next_node = current.next
        # 反转当前节点的指针
        current.next = prev
        # 移动指针
        prev = current
        current = next_node
    
    # prev指向新的头节点
    return prev


def print_list(node: ListNode) -> str:
    """
    打印链表
    
    Args:
        node: 链表的头节点
    
    Returns:
        链表的字符串表示
    """
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    return "->".join(result)


def build_list(values):
    """
    根据列表构建链表
    
    Args:
        values: 包含节点值的列表
    
    Returns:
        链表的头节点
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
        ([1], [1])
    ]
    
    for values, expected in test_cases:
        head = build_list(values)
        reversed_head = reverse_list(head)
        result = print_list(reversed_head)
        expected_str = "->".join(map(str, expected))
        print(f"Input: {values}")
        print(f"Expected: {expected_str}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected_str}")
        print("-" * 50)