"""
有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组nums中。
现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。
这里的 i - 1 和 i + 1 代表和i相邻的两个气球的序号。
如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
求所能获得硬币的最大数量。
思路：动态规划
dp[i][j]表示打爆 arr[i..j]所有气球的最大分数
base case:
递推：
"""

def maxCoin(nums):
    if not nums or len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    # arr 数组，方便开头和结尾元素的操作，与中间元素一样
    arr = [1] + nums + [1]
    n = len(arr)-2
    # dp
    dp = [[0] * (n+2) for _ in range(n+2)]
    # base case
    for i in range(1, n+1):
        dp[i][i] = arr[i-1] * arr[i] * arr[i+1]

    for L in range(n, 0, -1):
        for R in range(L+1, n+1):
            # 最后打爆 arr[L]
            final1 = arr[L-1] * arr[L] * arr[R+1] + dp[L+1][R]
            # 最后打爆 arr[R]
            final2 = arr[L-1] * arr[R] * arr[R+1] + dp[L][R-1]
            dp[L][R] = max(final1, final2)
            # 最后打爆位于 L, R 的中间位置元素 arr[i]
            for i in range(L+1, R):
                cur = arr[L-1] * arr[i] * arr[R+1] + dp[L][i-1] + dp[i+1][R]
                dp[L][R] = max(cur, dp[L][R])
    return dp[1][n]


def maxCoins2(nums):
    n = len(nums)
    rec = [[0] * (n+2) for _ in range(n+2)]
    val = [1] + nums + [1]

    for i in range(n-1, -1, -1):
        for j in range(i+2, n+2):
            for k in range(i+1, j):
                total = val[i] * val[k] * val[j]
                total += rec[i][k] + rec[k][j]
                rec[i][j] = max(rec[i][j], total)
    return rec[0][n+1]



def maxCoins3(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    https://leetcode-cn.com/problems/burst-balloons/solution/zhe-ge-cai-pu-zi-ji-zai-jia-ye-neng-zuo-guan-jian-/
    """
    #nums首尾添加1，方便处理边界情况
    nums.insert(0,1)
    nums.insert(len(nums),1)

    store = [[0]*(len(nums)) for i in range(len(nums))]

    def range_best(i,j):
        m = 0
        #k是(i,j)区间内最后一个被戳的气球
        for k in range(i+1,j): #k取值在(i,j)开区间中
            #以下都是开区间(i,k), (k,j)
            left = store[i][k]
            right = store[k][j]
            a = left + nums[i]*nums[k]*nums[j] + right
            if a > m:
                m = a
        store[i][j] = m

    #对每一个区间长度进行循环
    for n in range(2,len(nums)): #区间长度 #长度从3开始，n从2开始
        #开区间长度会从3一直到len(nums)
        #因为这里取的是range，所以最后一个数字是len(nums)-1

        #对于每一个区间长度，循环区间开头的i
        for i in range(0,len(nums)-n): #i+n = len(nums)-1

            #计算这个区间的最多金币
            range_best(i,i+n)

    return store[0][len(nums)-1]


if __name__ == "__main__":
    nums = [3, 1, 5, 8]
    print(maxCoin(nums))
