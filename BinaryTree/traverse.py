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
