"""
给定一个链表，反转链表。
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverseList(head):
    pre = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre

