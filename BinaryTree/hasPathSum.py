"""
给一个二叉树，一个整数 target。判断树种是否存在根节点到叶子节点的路径，这条路径和为 target。
思路：广度优先遍历
cur 记录从根节点遍历到当前节点的路径和
如果当前节点是叶子节点，比较 cur == target
如果不是叶子节点，那么将左右孩子节点加入队列。
"""
from collections import deque

def hasPathSum(root, target):
    if not root:
        return False

    q = deque()
    q.append((root, root.val))

    while q:
        node, cur = q.popleft()
        if not node.left and not node.right and cur == target:
            return True
        if node.left:
            q.append((node.left, node.left.val + cur))
        if node.right:
            q.append((node.right, node.right.val + cur))

    return False



# 输出路径
# DFS 深度优先遍历
# cur记录当前路径和，tmp记录当前路径上的节点
# 备注: [1] + [2] ==> [1, 2]
def pathSum(root, target):
    if not root:
        return []
    res = []

    def dfs(node, cur, tmp):
        if cur == target and not node.left and not node.right:
            res.append(tmp)
        if node.left:
            dfs(node.left, cur+node.left.val, tmp+[node.left.val])
        if node.right:
            dfs(node.right, cur+node.right.val, tmp+[node.right.val])

    dfs(root, root.val, [root.val])
    return res


# 广度优先遍历，在hasPathSum的基础上，加上当前路径节点即可
def pathSum2(root, targetSum):

    if not root:
        return []

    q = deque()
    q.append((root, root.val, [root.val]))
    res = []

    while q:
        node, cur, tmp = q.popleft()
        if not node.left and not node.right and cur == targetSum:
            res.append(tmp)
        if node.left:
            q.append((node.left, node.left.val + cur, tmp + [node.left.val]))
        if node.right:
            q.append((node.right, node.right.val + cur, tmp + [node.right.val]))

    return res