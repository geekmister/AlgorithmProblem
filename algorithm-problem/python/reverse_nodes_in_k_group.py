"""
K个一组翻转链表 (Reverse Nodes in k-Group)

问题描述：
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

使用场景：
- 链表操作
- 算法设计
- 数据结构的操作

算法难度：困难

时间复杂度：O(n) - 只需遍历链表一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- k 是一个正整数，它的值小于或等于链表的长度
- 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序
- 可以使用迭代的方法，每次处理k个节点
"""

from typing import Optional

# 定义链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    K个一组翻转链表
    
    Args:
        head: 链表的头节点
        k: 每组的节点数
    
    Returns:
        翻转后的链表
    """
    # 创建哑节点，简化处理
    dummy = ListNode(0)
    dummy.next = head
    
    # 初始化指针
    prev = dummy
    
    while True:
        # 检查剩余节点是否至少有k个
        tail = prev
        for i in range(k):
            tail = tail.next
            if not tail:
                return dummy.next
        
        # 保存下一组的头节点
        next_group = tail.next
        
        # 翻转当前组的节点
        curr = prev.next
        for i in range(k - 1):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        # 移动指针到下一组
        prev = curr
        prev.next = next_group


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
        ([1, 2, 3, 4, 5], 2, "2->1->4->3->5"),
        ([1, 2, 3, 4, 5], 3, "3->2->1->4->5"),
        ([1, 2, 3, 4, 5], 1, "1->2->3->4->5"),
        ([1], 1, "1")
    ]
    
    for values, k, expected in test_cases:
        head = build_list(values)
        result = reverse_k_group(head, k)
        result_str = print_list(result)
        print(f"Input: {values}, k = {k}")
        print(f"Expected: {expected}")
        print(f"Result: {result_str}")
        print(f"Pass: {result_str == expected}")
        print("-" * 50)