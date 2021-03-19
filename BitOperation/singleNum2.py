"""
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。
找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
"""


def singleNumber2(nums):
    e1 = 0
    e2 = 0

    for e in nums:
        e1 ^= e

    rightOne = e1 & (~e1 + 1)

    for e in nums:
        if e & rightOne != 0:
            e2 ^= e

    return [e2, e1 ^ e2]