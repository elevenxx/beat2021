"""
进阶问题，返回最大岛的面积
"""

def IslandArea(mat):
    if not mat or not mat[0]:
        return 0
    n, m = len(mat), len(mat[0])
    res = 0
    for i in range(0, n):
        for j in range(0, m):
            if mat[i][j] == 1:
                cur = infect(mat, i, j, n, m)
                res = max(res, cur)
    return res


def infect(mat, i, j, N, M):
    if i < 0 or i >= N or j < 0 or j >= M or mat[i][j] != 1:
        # 这个地方注意最后一个条件，应该放在最后，如果放在前面可能会造成数组越界
        return 0

    # 当前岛屿初始面积为1
    area = 1
    # 该块陆地已被算入岛屿面积中，做标记以免以后被重复计算
    mat[i][j] = 2

    area += infect(mat, i + 1, j, N, M)
    area += infect(mat, i - 1, j, N, M)
    area += infect(mat, i, j + 1, N, M)
    area += infect(mat, i, j - 1, N, M)
    return area


if __name__ == "__main__":
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(IslandArea(grid))
