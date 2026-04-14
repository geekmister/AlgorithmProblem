"""
合并K个升序链表 (Merge k Sorted Lists)

问题描述：
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

使用场景：
- 归并排序
- 多数据源的合并
- 算法设计

算法难度：困难

时间复杂度：O(n log k) - n是所有链表的总长度，k是链表的数量
空间复杂度：O(log k) - 递归调用栈的深度

其他信息：
- 可以使用分治的思想，将问题分解为合并两个链表的子问题
- 递归地合并两个链表，直到所有链表都被合并
- 这种方法的时间复杂度比逐个合并更高效
"""

from typing import List, Optional

# 定义链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    合并K个升序链表
    
    Args:
        lists: 链表数组
    
    Returns:
        合并后的升序链表
    """
    # 处理空数组的情况
    if not lists:
        return None
    
    # 处理只有一个链表的情况
    if len(lists) == 1:
        return lists[0]
    
    # 分治：将数组分成两部分
    mid = len(lists) // 2
    left = merge_k_lists(lists[:mid])
    right = merge_k_lists(lists[mid:])
    
    # 合并两个链表
    return merge_two_lists(left, right)


def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    合并两个升序链表
    
    Args:
        l1: 第一个升序链表
        l2: 第二个升序链表
    
    Returns:
        合并后的升序链表
    """
    # 创建哑节点作为新链表的头
    dummy = ListNode()
    current = dummy
    
    # 遍历两个链表
    while l1 and l2:
        # 比较两个节点的值，将较小的节点添加到新链表
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        # 移动当前指针
        current = current.next
    
    # 处理剩余的节点
    current.next = l1 if l1 else l2
    
    # 返回新链表的头节点
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
        ([
            build_list([1, 4, 5]),
            build_list([1, 3, 4]),
            build_list([2, 6])
        ], "1->1->2->3->4->4->5->6"),
        ([], ""),
        ([build_list([])], "")
    ]
    
    for lists, expected in test_cases:
        result = merge_k_lists(lists)
        result_str = print_list(result)
        print(f"Input: {[print_list(l) for l in lists]}")
        print(f"Expected: {expected}")
        print(f"Result: {result_str}")
        print(f"Pass: {result_str == expected}")
        print("-" * 50)