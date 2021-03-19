"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
思路：
回溯
"""

def subsets(nums):
    res = []
    n = len(nums)

    def helper(i, tmp):
        res.append(tmp)
        for j in range(i, n):
            helper(j+1, tmp+[nums[j]])

    helper(0, [])
    return res


if __name__ == "__main__":
    nums = [1, 2, 5]
    ans = subsets(nums)
    print(ans)
    print(len(ans))
