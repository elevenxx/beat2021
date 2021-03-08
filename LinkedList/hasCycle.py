"""
给定一个链表，判断是否有环。
思路：
快慢指针slow, fast
slow每次移动一步，fast两步。
如果链表无环，那么fast指针一定会先到达链表终点。
如果链表有环，那么slow和fast指针会在环中某个位置相遇。
此时将fast指针指向head，每次和slow同步移动一步，再次相遇的地方即为环的入口。
"""

def hasCycle(head):
    if not head or not head.next or not head.next.next:
        return None
    slow = head.next
    fast = head.next.next
    while slow != fast:
        if not fast.next or not fast.next.next:
            return None
        slow = slow.next
        fast = fast.next.next

    fast = head
    while slow != head:
        slow = slow.next
        fast = fast
    return slow

