"""
给两个单词，计算word1转换成word2所使用的最少操作数。
可以对一个单词进行如下三种操作：插入、删除、替换一个字符。
思路：
动态规划。
"""

def minDistance(w1, w2):
    m, n = len(w1), len(w2)
    if m * n == 0:
        return m + n

    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            left = dp[i][j-1] + 1
            down = dp[i-1][j] + 1
            left_down = dp[i-1][j-1]

            if w1[j-1] != w2[i-1]:
                left_down += 1

            dp[i][j] = min(left, down, left_down)

    return dp[n][m]


if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    print(minDistance(word1, word2))