"""
删除链表中的节点 (Delete Node in a Linked List)

问题描述：
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点 。

使用场景：
- 链表操作
- 数据结构的操作
- 算法设计

算法难度：简单

时间复杂度：O(1) - 只需要常数时间
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 该问题的特殊之处在于，我们只知道要删除的节点，而不知道其前一个节点
- 解决方法是将下一个节点的值复制到当前节点，然后删除下一个节点
- 该方法只适用于非末尾节点
"""

# 定义链表节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(node: ListNode) -> None:
    """
    删除链表中的节点
    
    Args:
        node: 要被删除的节点
    
    Returns:
        None，直接修改链表
    """
    # 将下一个节点的值复制到当前节点
    node.val = node.next.val
    # 删除下一个节点
    node.next = node.next.next


def print_list(head: ListNode) -> str:
    """
    打印链表
    
    Args:
        head: 链表的头节点
    
    Returns:
        链表的字符串表示
    """
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
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
        ([4, 5, 1, 9], 5, [4, 1, 9]),  # 删除值为5的节点
        ([4, 5, 1, 9], 1, [4, 5, 9])   # 删除值为1的节点
    ]
    
    for values, target_val, expected in test_cases:
        # 构建链表
        head = build_list(values)
        # 找到目标节点
        node = head
        while node and node.val != target_val:
            node = node.next
        # 删除节点
        delete_node(node)
        # 验证结果
        result = print_list(head)
        expected_str = "->".join(map(str, expected))
        print(f"Input: {values}, delete node: {target_val}")
        print(f"Expected: {expected_str}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected_str}")
        print("-" * 50)