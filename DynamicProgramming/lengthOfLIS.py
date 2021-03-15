"""
给一个整数数组 arr，找到其中最长严格递增子序列的长度。
"""

# 时间复杂度 O(N^2)
# dp[i] 代表以 arr[i]结尾的最长子序列长度
# 遍历数组，找到 arr[i] 左边比它小的元素 arr[j]
# 如果dp[j]+1 > dp[i]，更新当前dp[i]即可
def longestIncreasingSubsequence1(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
    return max(dp)


# 二分查找，时间复杂度降到O(NlogN)
# ends[k] 代表 所有 k+1 长度的子序列，最小的结尾数
def LIS(arr):
    ends = [0] * len(arr)
    ans = 0

    # 找到 e 在 ends 数组中可以存放的位置
    for e in arr:
        i, j = 0, ans

        while i < j:
            m = (i + j) // 2
            if ends[m] < e:
                i = m + 1
            else:
                j = m

        ends[i] = e
        if j == ans:
            ans += 1

    return ans