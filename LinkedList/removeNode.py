"""
给一个链表，和一个整数 val，删除链表中所有满足 node.val == val 的节点。
思路：
遇到满足条件的节点，就跳过，前一个节点直接连接下一个节点。
"""

# 定义链表节点
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 递归写法
def removeNode1(self, head, val):
    if not head:
        return None
    head.next = self.removeNode1(head.next, val)
    if head.val == val:
        return head.next
    else:
        return head


# 迭代写法
def removeNode2(self, head, val):
    if not head:
        return None
    dummy = ListNode(-1)
    dummy.next = head
    cur = dummy
    while cur:
        if cur.next and cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next