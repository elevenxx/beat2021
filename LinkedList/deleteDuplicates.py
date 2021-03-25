"""
存在一个按升序排列的链表，给你这个链表的头节点 head ，
请你删除链表中所有存在数字重复情况的节点，
只保留原始链表中没有重复出现的数字。
返回同样按升序排列的结果链表。
"""
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    if not head:
        return None

    dummy = ListNode(0, head)
    cur = dummy
    while cur.next and cur.next.next:
        if cur.next.val == cur.next.next.val:
            x = cur.next.val
            while cur.next and cur.next.val == x:
                cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next