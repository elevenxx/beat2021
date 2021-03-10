"""
给定一个字符串，返回它的最长回文子串。
"""


# 动态规划
# dp[i][j] 表示s[i..j] 是否是回文子串，左闭右闭区间包括s[i],s[j]
# 如果 s[i]==s[j],则dp[i][j] == dp[i+1][j-1]
def longestPalindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start, ans = 0, 1  # 记录最长回文子串的起点和长度

    if n < 2:
        return s
    for i in range(n):
        dp[i][i] = True

    # 枚举区间终点
    for j in range(1, n):
        # 枚举起点
        for i in range(j):
            if s[i] == s[j]:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]

            if dp[i][j]:
                lens = j - i + 1
                if lens > ans:
                    ans = lens
                    start = i
    return s[start:start + ans]


# 中心扩散，时间复杂度仍和DP一样，O(N^2)，但是空间复杂度降到O(1)
def longestPalindrome2(s):
    n = len(s)
    if n < 2:
        return s
    ans = 1  # 记录长度
    res = s[0]  # 记录子串

    for i in range(n):
        odd, oddlens = _center_spread(s, n, i, i)
        even, evenlens = _center_spread(s, n, i, i + 1)

        cur = odd if oddlens > evenlens else even
        if len(cur) > ans:
            ans = len(cur)
            res = cur
    return res

# 返回中心扩散的最长子串及长度
def _center_spread(s, size, left, right):
    i, j = left, right
    while i >= 0 and j < size and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i + 1: j], j - i + 1


if __name__ == "__main__":
    s = "babad"
    # s = "cbbd"
    print(longestPalindrome(s))
    print(longestPalindrome2(s))
