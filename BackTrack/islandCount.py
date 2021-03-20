"""
给一个二维数组，返回岛的数量
思路：
感染过程
从当前位置出发，把连成一片的1全部变成2
有多少次感染的过程，就有多少个岛
"""

def countIsland(mat):
    if not mat or not mat[0]:
        return 0
    n, m = len(mat), len(mat[0])
    res = 0
    for i in range(0, n):
        for j in range(0, m):
            if mat[i][j] == 1:
                res += 1
                infect(mat, i, j, n, m)
    return res

def infect(mat, i, j, N, M):
    if i < 0 or i >= N or j < 0 or j >= M or mat[i][j] != 1:
        # 这个地方注意最后一个条件，应该放在最后，如果放在前面可能会造成数组越界
        return
    mat[i][j] = 2
    infect(mat, i + 1, j, N, M)
    infect(mat, i - 1, j, N, M)
    infect(mat, i, j + 1, N, M)
    infect(mat, i, j - 1, N, M)



if __name__ == "__main__":
    # matrix = [[1, 0, 1, 1],
    #           [1, 0, 1, 1],
    #           [0, 0, 0, 0],
    #           [1, 0, 1, 0]]
    # print(countIsland(matrix))
    grid = [[1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]]
    print(countIsland(grid))



