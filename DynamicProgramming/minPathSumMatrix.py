"""
给定一个矩阵，从左上角到右下角位置，路径上所有数字累加起来就是路径和。
返回所有路径中最小的路径和。
思路：
dp[i][j]代表从(0,0)位置走到(i,j)位置的最小路径和
递归方程 dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
第一行，只能从(0,0)位置往右走，dp[0][i]=dp[0][i-1]+matrix[0][i]
第一列，只能从(0,0)往下走
"""

def minPathSumMatrix(m):
    if not m or len(m) == 0 or not m[0] or len(m[0]) == 0:
        return 0

    row = len(m)
    col = len(m[0])

    dp = [[0] * col for _ in range(row)]
    dp[0][0] = m[0][0]

    for i in range(1, col):
        dp[0][i] = dp[0][i-1] + m[0][i]

    for j in range(1, row):
        dp[j][0] = dp[j-1][0] + m[j][0]

    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + m[i][j]

    # return dp[row-1][col-1]
    return dp[-1][-1]