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


# 路径无需从根节点开始，也不需要在叶子节点结束，路径方向向下即可。
# 思路：DFS遍历，在遍历的过程中每搜寻一个新节点，都计算一次从根节点到当前节点的路径和，使用哈希表存储数值。
# hashmap[x] = y 代表路径和为x的路径有y条
# 寻找子路径：判断cur-target 是否在hashmap中存储过，存储过几次就说明存在几条路径

from collections import defaultdict

def pathSumNoRoot(root, target):
    hashmap = defaultdict(int)
    hashmap[0] = 1

    def dfs(root, cur):
        if not root:
            return 0
        cur += root.val
        cnt = hashmap[cur - target]
        hashmap[cur] += 1
        leftcnt = dfs(root.left, cur)
        rightcnt = dfs(root.right, cur)
        hashmap[cur] -= 1

        return cnt + leftcnt + rightcnt

    return dfs(root, 0, hashmap)
