"""
给定一个字符串，返回最长无重复字符子串的长度。
"""

def lengthOfLongestSubstring(s):
    last = {}  # 记录字符是否在当前子串出现过
    ans = 0
    left = 0   # 无重复子串最左边的位置
    for i in range(len(s)):
        if s[i] in last and last[s[i]] >= left:   # s[i]出现过且在当前子串中
            left = last[s[i]] + 1                 # 更新左边界
        last[s[i]] = i                            # 更新s[i]在当前子串的位置
        ans = max(ans, i-left+1)                  # 更新长度
    return ans
