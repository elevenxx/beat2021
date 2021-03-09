"""
返回两个单链表的相交节点，若无，则返回None
思路：
指针pA,pB
先各自从自己的链表头开始走，走到结尾，接着从对方的链表头开始走。
相遇的地方即为相交节点。
pA走过A+B，pB走过B+A
若A，B的结尾部分相同，那么，A+B和B+A的结尾部分也是相同的。
若无相交，那么pA和pB结束时都指向None
"""


def getIntersection(headA, headB):
    pA, pB = headA, headB
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    return pA