"""
二叉树的前序遍历、中序遍历、后序遍历、层序遍历
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preOrder1(self, root):
    return [root.val] + self.preOrder1(root.left) + self.preOrder1(root.right) if root else []


def preOrder(root):
    print("pre-order: ")
    ans = []
    if root:
        stk = [root]
        while stk:
            node = stk.pop()
            ans.append(node.val)
            if node.right:
                stk.append(node.right)
            if node.left:
                stk.append(node.left)
    return ans


# 先打印左子树，打印头结点，再打印右子树
def inOrder(root):
    print("in-order: ")
    ans = []
    if root:
        stk = []
        while stk or root:
            if root:
                stk.append(root)
                root = root.left
            else:
                root = stk.pop()
                ans.append(root.val)
                root = root.right
    return ans


from collections import deque


# 按层遍历
def levelOrder(root):
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        level = []
        n = len(q)
        for _ in range(q):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res

# zigzag
def zigzagLevelOrder(root):
    if not root:
        return []

    q = deque([root])
    res = []
    flag = False

    while q:
        level = []
        n = len(q)

        for _ in range(n):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        flag = ~flag
        if flag:
            res.append(level)
        else:
            res.append(level[::-1])

    return res
