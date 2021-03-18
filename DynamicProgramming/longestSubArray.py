"""
给定两个字符串，返回最长公共子串（连续的）
思路：
动态规划
dp[i][j]代表在必须把str1[i]和str2[j]当作公共子串最后一个字符的情况下，公共子串最长有多长
"""

def longestSubarray(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * n for _ in range(m)]
    for i in range(0, m):
        if str1[i] == str2[0]:
            dp[i][0] = 1
    for j in range(0, n):
        if str2[j] == str1[0]:
            dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1] + 1

    return dp