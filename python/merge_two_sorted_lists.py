"""
合并两个有序链表 (Merge Two Sorted Lists)

问题描述：
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

使用场景：
- 归并排序中的合并操作
- 合并多个有序数据集
- 数据库查询结果的合并

算法难度：简单

时间复杂度：O(n+m) - n和m分别是两个链表的长度
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 可以使用递归或迭代的方法
- 迭代方法通常更高效，因为避免了递归调用的开销
- 需要考虑其中一个链表为空的情况
"""

# 定义链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    合并两个有序链表
    
    Args:
        l1: 第一个有序链表
        l2: 第二个有序链表
    
    Returns:
        合并后的有序链表
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
        node: 链表头节点
    
    Returns:
        链表的字符串表示
    """
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    return "->".join(result)


if __name__ == "__main__":
    # 测试用例
    # 构建测试链表1: 1->2->4
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    
    # 构建测试链表2: 1->3->4
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    
    # 测试用例1
    result1 = merge_two_lists(l1, l2)
    print("Test Case 1:")
    print(f"Input: l1 = 1->2->4, l2 = 1->3->4")
    print(f"Expected: 1->1->2->3->4->4")
    print(f"Result: {print_list(result1)}")
    print("-" * 50)
    
    # 测试用例2: 空链表
    l3 = None
    l4 = None
    result2 = merge_two_lists(l3, l4)
    print("Test Case 2:")
    print(f"Input: l1 = None, l2 = None")
    print(f"Expected: None")
    print(f"Result: {print_list(result2) if result2 else 'None'}")
    print("-" * 50)
    
    # 测试用例3: 一个空链表
    l5 = None
    l6 = ListNode(0)
    result3 = merge_two_lists(l5, l6)
    print("Test Case 3:")
    print(f"Input: l1 = None, l2 = 0")
    print(f"Expected: 0")
    print(f"Result: {print_list(result3)}")
    print("-" * 50)