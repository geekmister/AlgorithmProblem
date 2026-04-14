"""
旋转链表 (Rotate List)

问题描述：
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置。

使用场景：
- 链表操作
- 算法设计
- 数据结构的操作

算法难度：中等

时间复杂度：O(n) - 只需遍历链表两次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 可以先计算链表的长度，然后将链表首尾相连，形成一个环
- 找到新的头节点和尾节点，断开环
- 需要考虑k大于链表长度的情况，可以取模
"""

from typing import Optional

# 定义链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    旋转链表，将链表每个节点向右移动k个位置
    
    Args:
        head: 链表的头节点
        k: 移动的位置数
    
    Returns:
        旋转后的链表
    """
    # 处理空链表或只有一个节点的情况
    if not head or not head.next:
        return head
    
    # 计算链表的长度
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    
    # 计算实际需要移动的位置
    k = k % length
    if k == 0:
        return head
    
    # 将链表首尾相连，形成一个环
    tail.next = head
    
    # 找到新的尾节点（距离原头节点 length - k - 1 步）
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
    
    # 新的头节点是新尾节点的下一个节点
    new_head = new_tail.next
    
    # 断开环
    new_tail.next = None
    
    return new_head


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
        ([1, 2, 3, 4, 5], 2, "4->5->1->2->3"),
        ([0, 1, 2], 4, "2->0->1"),  # 4 % 3 = 1
        ([1], 0, "1"),
        ([1, 2], 1, "2->1")
    ]
    
    for values, k, expected in test_cases:
        head = build_list(values)
        result = rotate_right(head, k)
        result_str = print_list(result)
        print(f"Input: {values}, k = {k}")
        print(f"Expected: {expected}")
        print(f"Result: {result_str}")
        print(f"Pass: {result_str == expected}")
        print("-" * 50)