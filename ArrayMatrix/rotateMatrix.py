"""
给一个NxN的矩阵，把这个矩阵顺时针转动90°
思路：
和转圈打印矩阵类似
一圈圈的调整坐标
该圈的长宽为 M 时，需要 M-1 次调整
"""


def rotate(matrix):
    tx, ty = 0, 0
    dx, dy = len(matrix) - 1, len(matrix[0]) - 1
    while tx < dx:
        rotateEdge(matrix, tx, ty, dx, dy)
        tx, ty, dx, dy = tx + 1, ty + 1, dx - 1, dy - 1
    print(matrix)


def rotateEdge(m, tx, ty, dx, dy):
    times = dx - tx
    for i in range(times):  # 一次循环就是一次调整，四个点交换坐标值
        # 上、右、下、左 四个点的坐标：
        # m[tx][ty+i], m[tx+i][dy], m[dx][dy-i], m[dx-i][ty]
        tmp = m[tx][ty + i]
        m[tx][ty + i] = m[dx - i][ty]
        m[dx - i][ty] = m[dx][dy - i]
        m[dx][dy - i] = m[tx + i][dy]
        m[tx + i][dy] = tmp


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    rotate(matrix)
