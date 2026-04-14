"""
相交链表 (Intersection of Two Linked Lists)

问题描述：
编写一个程序，找到两个单链表相交的起始节点。

使用场景：
- 链表操作
- 数据结构的分析
- 算法设计

算法难度：简单

时间复杂度：O(n+m) - n和m分别是两个链表的长度
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 可以使用双指针技术
- 让两个指针分别从两个链表的头节点出发，当其中一个指针到达链表末尾时，转向另一个链表的头节点继续遍历
- 当两个指针相遇时，就是相交的起始节点
"""

# 定义链表节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_intersection_node(headA: ListNode, headB: ListNode) -> ListNode:
    """
    找到两个链表相交的起始节点
    
    Args:
        headA: 第一个链表的头节点
        headB: 第二个链表的头节点
    
    Returns:
        相交的起始节点，如果没有相交则返回None
    """
    # 处理空链表的情况
    if not headA or not headB:
        return None
    
    # 初始化两个指针
    ptrA = headA
    ptrB = headB
    
    # 当两个指针不相等时继续遍历
    while ptrA != ptrB:
        # 当指针到达链表末尾时，转向另一个链表的头节点
        ptrA = ptrA.next if ptrA else headB
        ptrB = ptrB.next if ptrB else headA
    
    # 当两个指针相等时，就是相交的起始节点或None
    return ptrA


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
    # 测试用例：相交的情况
    # 构建相交的链表
    # 链表A: 1->2->3->4->5
    # 链表B: 6->7->3->4->5
    # 相交点是3
    common = build_list([3, 4, 5])
    headA = build_list([1, 2])
    headA.next.next = common
    headB = build_list([6, 7])
    headB.next.next = common
    
    intersection = get_intersection_node(headA, headB)
    print("Test Case 1: Intersecting Lists")
    print(f"List A: {print_list(headA)}")
    print(f"List B: {print_list(headB)}")
    print(f"Intersection: {intersection.val if intersection else 'None'}")
    print(f"Expected: 3")
    print(f"Pass: {intersection and intersection.val == 3}")
    print("-" * 50)
    
    # 测试用例：不相交的情况
    headA = build_list([1, 2, 3])
    headB = build_list([4, 5, 6])
    
    intersection = get_intersection_node(headA, headB)
    print("Test Case 2: Non-intersecting Lists")
    print(f"List A: {print_list(headA)}")
    print(f"List B: {print_list(headB)}")
    print(f"Intersection: {intersection.val if intersection else 'None'}")
    print(f"Expected: None")
    print(f"Pass: {intersection is None}")
    print("-" * 50)
    
    # 测试用例：一个链表为空的情况
    headA = build_list([1, 2, 3])
    headB = None
    
    intersection = get_intersection_node(headA, headB)
    print("Test Case 3: One empty list")
    print(f"List A: {print_list(headA)}")
    print(f"List B: None")
    print(f"Intersection: {intersection.val if intersection else 'None'}")
    print(f"Expected: None")
    print(f"Pass: {intersection is None}")
    print("-" * 50)