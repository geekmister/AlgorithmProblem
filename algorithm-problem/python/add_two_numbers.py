"""
两数相加 (Add Two Numbers)

问题描述：
给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。

使用场景：
- 链表操作
- 大数相加
- 算法设计

算法难度：中等

时间复杂度：O(max(m, n)) - m和n分别是两个链表的长度
空间复杂度：O(max(m, n)) - 需要存储结果链表

其他信息：
- 链表中的每个节点存储一个数字，按照逆序排列
- 需要考虑进位的情况
- 两个链表的长度可能不同
- 最后一位相加后可能还有进位
"""

from typing import Optional

# 定义链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    相加两个链表表示的数
    
    Args:
        l1: 第一个链表
        l2: 第二个链表
    
    Returns:
        表示和的链表
    """
    # 创建虚拟头节点
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    # 遍历两个链表
    while l1 or l2 or carry:
        # 计算当前位的和
        sum_val = carry
        if l1:
            sum_val += l1.val
            l1 = l1.next
        if l2:
            sum_val += l2.val
            l2 = l2.next
        
        # 计算当前位的值和进位
        carry = sum_val // 10
        current.next = ListNode(sum_val % 10)
        current = current.next
    
    # 返回结果链表
    return dummy.next

def build_linked_list(values):
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

def linked_list_to_list(head: Optional[ListNode]) -> list:
    """
    将链表转换为列表
    
    Args:
        head: 链表的头节点
    
    Returns:
        包含节点值的列表
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    
    return result


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),  # 342 + 465 = 807
        ([0], [0], [0]),  # 0 + 0 = 0
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1])  # 9999999 + 9999 = 10009998
    ]
    
    for values1, values2, expected in test_cases:
        l1 = build_linked_list(values1)
        l2 = build_linked_list(values2)
        result = add_two_numbers(l1, l2)
        result_list = linked_list_to_list(result)
        print(f"Input: l1={values1}, l2={values2}")
        print(f"Expected: {expected}")
        print(f"Result: {result_list}")
        print(f"Pass: {result_list == expected}")
        print("-" * 50)