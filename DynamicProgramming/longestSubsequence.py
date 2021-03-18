"""
给定两个字符串，返回最长公共子串（可不连续的）
str1 = '1A2B3C4D'
str2 = 'B1D23CA46'
返回'1234'
思路：
动态规划
len(str1)=M, len(str2)=N
生成一个MxN的矩阵dp,dp[i][j]的含义是str1[0..i]与str2[0..j]的最长公共子序列的长度
从左到右，再从上到下计算矩阵dp
"""

def longSubsequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1 if str1[0] == str2[0] else 0

    for i in range(1, m):
        dp[i][0] = 1 if str1[i] == str2[0] else 0
        dp[i][0] = max(dp[i][0], dp[i-1][0])

    for j in range(1, n):
        dp[0][j] = 1 if str1[0] == str2[j] else 0
        dp[0][j] = max(dp[0][j], dp[0][j-1])

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if str1[i] == str2[j]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
    return dp