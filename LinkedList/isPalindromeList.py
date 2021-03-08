"""
给定一个链表，判断它是否是回文链表。
思路：
使用快慢指针遍历链表，找到中间位置节点。
慢指针遍历过程中反转前半部分链表。
比较前后两部分链表的节点值。
"""

def isPadlindrome(head):
    pre = None
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        nxt = slow.next
        slow.next = pre
        pre = slow
        slow = nxt
    if fast:
        slow = slow.next
    while pre and pre.val == slow.val:
        slow = slow.next
        pre = pre.next
    return not pre