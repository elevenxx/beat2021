"""
给定不同面额的硬币 coins,一个总金额 amount，计算可以凑成总金额所需的最少的硬币个数。
没有一种硬币组合能凑成总金额，返回 -1.
可以认为每种硬币的数量无限。
coins = [1,2,5], amount = 11
output: 3 (11 = 5 + 5 + 1)
思路：
自底向上的动态规划
memo[i]表示凑成总金额为 i 所需的最少的硬币数量
初始值为 amount+1，表示不可能凑到总金额的情况
memo[i]有两种实现方式：取两者最小值：
1) 包含当前 coins[i]，剩余钱 i-coins[j]，此操作对应的兑换硬币数为 memo[i-coins[j]] + 1
coins[j]表示 coins 数组中每种面值
2) 不包含，要兑换的硬币数是 memo[i]
"""

def coinChange(coins, amount):
    if not coins or len(coins) == 0:
        return -1
    memo = [amount+1] * (amount+1)
    memo[0] = 0

    # for i in range(1, amount+1):
    #   for j in range(len(coins)):
    #        if i - coins[j] >= 0:
    #            memo[i] = min(memo[i], memo[i-coins[j]] + 1)

    for i in range(1, amount + 1):
        for j in coins:
            if i >= j:
                memo[i] = min(memo[i], memo[i - j] + 1)

    if memo[-1] == amount + 1:
        return -1
    else:
        return memo[-1]

# DFS
# 优先选择大面值的硬币，先对数组排序。
# 最先找到的解法不一定是最优解，比如[1,7,10],14 = 10+1+1+1+1 = 7+7
# 所以需要遍历所有情况
# 关键是剪枝：找到一种解法后，记录硬币数，随后的所有遍历只要硬币数比之前多，就剪枝

def coinChange(self, coins, amount):
    n = len(coins)
    coins.sort(reverse=True)
    self.res = float('inf')

    def dfs(index, target, count):
        coin = coins[index]

        if target // coin + count >= self.res:  # 剪枝条件
            return
        if target % coin == 0:
            self.res = count + target // coin
            return

        if index == n - 1:  # 注意顺序，放在三个if最后，因为使用最后一种硬币可能会出现更小的硬币数量，因此不能放在最前面
            return

        for j in range(target//coin, -1, -1):  # DFS
            dfs(index+1, target-j*coin, count+j)

    dfs(0, amount, 0)
    return self.res if self.res != float('inf') else -1