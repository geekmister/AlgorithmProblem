"""
环形链表 (Linked List Cycle)

问题描述：
给定一个链表，判断链表中是否有环。

使用场景：
- 链表操作
- 数据结构的分析
- 算法设计

算法难度：简单

时间复杂度：O(n) - 只需遍历链表一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 可以使用快慢指针技术（Floyd's Cycle-Finding Algorithm）
- 快指针每次走两步，慢指针每次走一步
- 如果链表中有环，快慢指针最终会相遇
"""

# 定义链表节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head: ListNode) -> bool:
    """
    判断链表中是否有环
    
    Args:
        head: 链表的头节点
    
    Returns:
        是否有环
    """
    # 处理空链表或只有一个节点的情况
    if not head or not head.next:
        return False
    
    # 初始化快慢指针
    slow = head
    fast = head.next
    
    # 当快慢指针不相等时继续遍历
    while slow != fast:
        # 如果快指针到达链表末尾，说明没有环
        if not fast or not fast.next:
            return False
        # 慢指针走一步，快指针走两步
        slow = slow.next
        fast = fast.next.next
    
    # 快慢指针相遇，说明有环
    return True


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
        ([3, 2, 0, -4], 1, True),  # 有环，环的起始位置是1
        ([1, 2], 0, True),  # 有环，环的起始位置是0
        ([1], -1, False)  # 无环
    ]
    
    for values, pos, expected in test_cases:
        head = build_list_with_cycle(values, pos)
        result = has_cycle(head)
        print(f"Input: values = {values}, pos = {pos}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)