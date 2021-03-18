"""
给定两个字符串str1, str2，三个整数ic,dc,rc，分别代表插入、删除、替换一个字符的代价
返回将str1编辑成str2的最小代价
思路：
动态规划
m, n = len(str1), len(str2)
dp： m+1 行 n+1 列
dp[i][j]的值代表 str1[0..i-1]编辑成 str2[0..j-1]的最小代价
base case:
dp[i][0]代表str1[0..i-1]编辑成空串的代价，dp[i][0]=dc*i
dp[0][j]代表从空串到str2[0..j-1]的代价，dp[0][j]=ic*j
其他位置从左到右，从上到下
dp[i][j] = min(dp[i-1][j]+dc, dp[i][j-1]+ic, dp[i-1][j-1] + rc/0 see if str1[i-1] ?= str2[j-1])
"""

def minEditCost(str1, str2, dc, ic, rc):
    if not str1 or not str2:
        return 0
    m, n = len(str1), len(str2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        dp[i][0] = dc * i

    for j in range(1, n+1):
        dp[0][j] = ic * j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + rc

            dp[i][j] = min(dp[i][j],
                           dp[i-1][j] + dc,
                           dp[i][j-1] + ic
            )

    return dp[-1][-1]