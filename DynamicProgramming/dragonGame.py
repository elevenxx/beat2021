"""
给定一个二维数组 m 代表地图，要保证骑士从左上角出发到达右下角见到公主。
每个位置的值代表骑士要遭遇的事情。负数要失血，正数会加血。
规定走到任何一个位置，血量不能少于1.
为了保证骑士见到公主，初始血量至少是多少？
思路：
定义一个和地图大小一样的dp数组，dp[i][j]代表从位置(i,j)到达右下角至少需要的血量，最后求dp[0][0]。
如果向右走，那么dp[i][j]至少要有dp[i][j+1]-m[i][j]的血量（因为要走到(i,j+1)，dp[i][j]+m[i][j]>=dp[i][j+1]）
同理，如果向下走，那么dp[i][j]至少要有dp[i+1][j]-m[i][j]的血量。
dp[i][j]取向右走或向下走的最小值。
dp更新方式为从右至左，从下到上。
"""

def dragonGame(m):
    if not m or len(m) == 0 or not m[0] or len(m[0]) == 0:
        return 1
    row, col = len(m), len(m[0])
    dp = [[1] * col for _ in range(row)]

    # 在右下角位置需要的血量，根据m[-1][-1]的正负不同，赋值不同
    dp[-1][-1] = 1 if m[-1][-1] > 0 else -m[-1][-1] + 1

    # 最后一行的赋值
    for j in range(col-2, -1, -1):
        dp[-1][j] = max(dp[-1][j+1] - m[-1][j], 1)

    # 先从右到左，再从上到下，所以row循环在外，col循环在内
    for i in range(row-2, -1, -1):
        # 当前行最后一列位置的血量(只能往下走，不能往右走，因为是最后一列了)
        dp[i][-1] = max(dp[i+1][-1] - m[i][-1], 1)

        # 填这一行
        for j in range(col-2, -1, -1):
            right = max(dp[i][j+1] - m[i][j], 1)
            down = max(dp[i+1][j] - m[i][j], 1)
            dp[i][j] = min(right, down)

    return dp[0][0]


if __name__ == "__main__":
    m = [[-2, -3, 3],
         [-5, -10, 1],
         [0, 30, -5]]
    print(dragonGame(m))