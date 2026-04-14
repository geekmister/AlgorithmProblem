"""
删除链表的倒数第N个节点 (Remove Nth Node From End of List)

问题描述：
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

使用场景：
- 链表操作
- 双指针技术
- 算法设计

算法难度：中等

时间复杂度：O(n) - 只需遍历链表一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 可以使用双指针技术，让快指针先走n步，然后快慢指针同时移动，当快指针到达链表末尾时，慢指针指向的就是倒数第n个节点的前一个节点
- 需要考虑删除头节点的情况，可以使用哑节点来简化处理
- 需要考虑链表长度小于n的情况（题目假设n是有效的）
"""

# 定义链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    """
    删除链表的倒数第n个节点
    
    Args:
        head: 链表的头节点
        n: 倒数第n个节点
    
    Returns:
        删除后的链表头节点
    """
    # 创建哑节点，简化删除头节点的情况
    dummy = ListNode(0)
    dummy.next = head
    
    # 初始化快慢指针
    fast = dummy
    slow = dummy
    
    # 快指针先走n+1步
    for _ in range(n + 1):
        fast = fast.next
    
    # 快慢指针同时移动，直到快指针到达链表末尾
    while fast:
        fast = fast.next
        slow = slow.next
    
    # 删除倒数第n个节点
    slow.next = slow.next.next
    
    # 返回新的头节点
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
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),  # 删除倒数第2个节点
        ([1], 1, []),  # 删除唯一的节点
        ([1, 2], 1, [1])  # 删除倒数第1个节点
    ]
    
    for values, n, expected in test_cases:
        head = build_list(values)
        result_head = remove_nth_from_end(head, n)
        result = print_list(result_head)
        expected_str = "->".join(map(str, expected))
        print(f"Input: {values}, n = {n}")
        print(f"Expected: {expected_str}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected_str}")
        print("-" * 50)