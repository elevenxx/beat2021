"""
给定一个数组arr，元素任意。返回子数组最大累乘积。
思路：
遍历数组，记录以当前元素arr[i]结尾的子数组的最大/最小累乘积。
记录最小是因为后面可能会出现负负得正的结果。
"""


def maxProduct(arr):
    curmax, curmin = 1, 1
    ans = arr[0]
    for c in arr:
        if c < 0:
            curmax, curmin = curmin, curmax
        curmax = max(curmax*c, c)
        curmin = min(curmin*c, c)
        ans = max(ans, curmax)
    return ans


if __name__ == "__main__":
    A = [2,3,-2,4,-5,-99]
    print(maxProduct(A))