"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

#链接：https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-powcai/

"""

def longestValidParentheses(self, s: str) -> int:
    n = len(s)
    if n == 0: return 0
    dp = [0] * n
    res = 0
    for i in range(n):
        if i > 0 and s[i] == ")":
            if s[i - 1] == "(":
                dp[i] = dp[i - 2] + 2
            elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
            if dp[i] > res:
                res = dp[i]
    return res