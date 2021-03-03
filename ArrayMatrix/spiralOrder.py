"""
给一个矩阵，按照转圈的方式打印
思路：
矩阵左上角坐标(tx, ty),右下角坐标(dx, dy)，表示矩阵
打印矩阵外层一圈后，令tx+1, ty+1, dx-1, dy-1
新的左上角、右下角坐标表示子矩阵，再转圈打印
直到左上角坐标跑到右下角坐标的右边或下面
"""


def spiralOrderPrint(matrix):
    tx, ty = 0, 0
    dx, dy = len(matrix) - 1, len(matrix[0]) - 1
    tmp = []
    while tx <= dx and ty <= dy:
        printEdge(matrix, tx, ty, dx, dy, tmp)
        tx, ty, dx, dy = tx + 1, ty + 1, dx - 1, dy - 1
    print(tmp)


def printEdge(m, tx, ty, dx, dy, tmp):
    ans = []
    if tx == dx:  # 只有一行
        for i in range(ty, dy + 1):
            ans.append(m[tx][i])

    elif ty == dy:  # 只有一列
        for i in range(tx, dx + 1):
            ans.append(m[i][ty])

    else:  # 一般情况，转圈打印外层
        # 左上角(tx, ty),右上角(tx, dy),左下角(dx,ty),右下角(dx,dy)
        curx, cury = tx, ty
        while cury != dy:
            ans.append(m[tx][cury])
            cury += 1
        while curx != dx:
            ans.append(m[curx][dy])
            curx += 1
        while cury != ty:
            ans.append(m[dx][cury])
            cury -= 1
        while curx != tx:
            ans.append(m[curx][ty])
            curx -= 1
    tmp.extend(ans)


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]
              ]
    spiralOrderPrint(matrix)
