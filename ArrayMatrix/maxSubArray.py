"""
给定一个数组，返回子数组的最大累加和。
思路：
变量cur记录到达当前元素时，包含当前元素的子数组的最大值。
两种情况：之前的子数组和小于0，或者大于等于0.
情况一：小于0时，重新开始计算。即此时只包含当前元素。
ans记录遍历过程中出现过的最大累加和。
"""

def maxSubArray(arr):
    cur = 0
    ans = arr[0]
    for e in arr:
        cur = max(cur+e, e)
        ans = max(ans, cur)
    return ans


if __name__ == "__main__":
    A = [1, -2, 3, 5, -2, 6, -1]
    print(maxSubArray(A))