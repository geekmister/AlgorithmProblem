"""
环形链表 II (Linked List Cycle II)

问题描述：
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

使用场景：
- 链表操作
- 数据结构的分析
- 算法设计

算法难度：中等

时间复杂度：O(n) - 只需遍历链表一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 可以使用快慢指针技术（Floyd's Cycle-Finding Algorithm）
- 快指针每次走两步，慢指针每次走一步
- 当快慢指针相遇后，将其中一个指针移到链表头部，然后两个指针以相同速度移动，再次相遇的位置就是环的起始节点
"""

# 定义链表节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detect_cycle(head: ListNode) -> ListNode:
    """
    找到链表开始入环的第一个节点
    
    Args:
        head: 链表的头节点
    
    Returns:
        环的起始节点，如果无环则返回None
    """
    # 处理空链表或只有一个节点的情况
    if not head or not head.next:
        return None
    
    # 初始化快慢指针
    slow = head
    fast = head
    
    # 找到快慢指针的相遇点
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    # 如果没有相遇，说明无环
    if slow != fast:
        return None
    
    # 将其中一个指针移到链表头部，然后两个指针以相同速度移动
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    # 再次相遇的位置就是环的起始节点
    return slow


def build_list_with_cycle(values, pos):
    """
    根据列表构建带环的链表
    
    Args:
        values: 包含节点值的列表
        pos: 环的起始位置（-1表示无环）
    
    Returns:
        链表的头节点
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    cycle_node = None
    
    # 构建链表
    for i, val in enumerate(values[1:]):
        current.next = ListNode(val)
        current = current.next
        # 记录环的起始位置
        if i == pos - 1:
            cycle_node = current
    
    # 创建环
    if pos != -1:
        current.next = cycle_node
    
    return head


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([3, 2, 0, -4], 1, 2),  # 环的起始位置是1，对应值为2
        ([1, 2], 0, 1),  # 环的起始位置是0，对应值为1
        ([1], -1, None)  # 无环
    ]
    
    for values, pos, expected_val in test_cases:
        head = build_list_with_cycle(values, pos)
        result = detect_cycle(head)
        result_val = result.val if result else None
        print(f"Input: values = {values}, pos = {pos}")
        print(f"Expected: {expected_val}")
        print(f"Result: {result_val}")
        print(f"Pass: {result_val == expected_val}")
        print("-" * 50)