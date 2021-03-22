"""
给一个数，返回其二进制位中的 1 的数量
思路：
n & (n-1) 的结果就是把 n 的二进制位的最低位的 1 变为 0
利用该性质，不断让当前的 n 与 n-1 做与运算，直到 n 变为 0 即可。
因为每次运算会使得 n 的最低位的 1 被翻转，因此运算次数就等于 n 的二进制位中 1 的个数
"""

def hammingWeight(n):
    res = 0
    while n:
        n &= (n-1)
        res += 1
    return res


if __name__ == "__main__":
    n = 6
    print(hammingWeight(n))