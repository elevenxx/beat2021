"""
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
"""

def setZeroes(matrix):
    row, col = len(matrix), len(matrix[0])
    r = set()
    c = set()
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                r.add(i)
                c.add(j)

    for i in range(row):
        for j in range(col):
            if i in r or j in c:
                matrix[i][j] = 0
    return matrix


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(setZeroes(matrix))