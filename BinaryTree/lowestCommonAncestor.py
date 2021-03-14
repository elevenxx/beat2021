"""
给定一个二叉树，找到该树中两个指定节点的最近公共祖先
"""

# 递归方法
def LCA(self, root, p, q):
    if not root or root == p or root == q:
        return root
    left = self.LCA(root.left, p, q)
    right = self.LCA(root.right, p, q)
    if not left:
        return right
    if not right:
        return left
    return root
