"""
两两交换链表中的节点 (Swap Nodes in Pairs)

问题描述：
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

使用场景：
- 链表操作
- 算法设计
- 数据结构的操作

算法难度：中等

时间复杂度：O(n) - 只需遍历链表一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换
- 可以使用哑节点来简化处理
- 需要考虑链表长度为奇数的情况
"""

from typing import Optional

# 定义链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    两两交换链表中的节点
    
    Args:
        head: 链表的头节点
    
    Returns:
        交换后的链表
    """
    # 创建哑节点，简化处理
    dummy = ListNode(0)
    dummy.next = head
    
    # 初始化指针
    prev = dummy
    
    # 当有至少两个节点时进行交换
    while prev.next and prev.next.next:
        # 保存要交换的两个节点
        first = prev.next
        second = prev.next.next
        
        # 交换节点
        first.next = second.next
        second.next = first
        prev.next = second
        
        # 移动指针到下一组
        prev = first
    
    return dummy.next


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
        ([1, 2, 3, 4], "2->1->4->3"),
        ([], ""),
        ([1], "1"),
        ([1, 2, 3], "2->1->3")
    ]
    
    for values, expected in test_cases:
        head = build_list(values)
        result = swap_pairs(head)
        result_str = print_list(result)
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result_str}")
        print(f"Pass: {result_str == expected}")
        print("-" * 50)