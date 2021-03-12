"""
验证一个二叉树是否是搜索二叉树
思路：
在中序遍历的基础上判断前一个元素值与当前元素值的大小
中序遍历序列是否是递增的
"""

def isBST(root):
    if root:
        stk = []
        pre = float('-inf')
        while stk or root:
            if root:
                stk.append(root)
                root = root.left
            else:
                root = stk.pop()
                cur = root.val
                if cur < pre:
                    return False
                root = root.right
                pre = cur

    return True