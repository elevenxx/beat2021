"""
给定不同面额的硬币 coins,一个总金额 amount，计算可以凑成总金额的组合数量。
假设每一种面额的硬币无限。
思路：
动态规划，dp[i]代表金额为 i 时的组合数量
base case: dp[0]=1，金额为0时组合数为1，即不使用任何硬币
递推：dp[i] = dp[i]+dp[i-coin]
"""

def coinSum(coins, amount):
    dp = [0] * (amount+1)
    dp[0] = 1

    for coin in coins:  # 这个地方for循环，遍历coin在前，因为这里计算的是组合数，2,1,2和1,2,2是一种组合。
        for x in range(coin, amount+1):
            dp[x] += dp[x-coin]
    return dp[-1]


# ref:https://leetcode-cn.com/problems/coin-change-2/solution/ling-qian-dui-huan-iihe-pa-lou-ti-wen-ti-dao-di-yo/