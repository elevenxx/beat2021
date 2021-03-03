"""
给定一个矩阵，按照之字形的方式打印。
在方阵中即为对角线遍历。
思路：
用两个坐标，上坐标和下坐标，连线即为矩阵的一条斜线，打印斜线上的元素
上坐标(tr,tc)初始为(0,0),先沿着矩阵第一行移动(tc++),当到达第一行最右边的元素时，再沿着矩阵最后一列移动(tr++)
下坐标(dr,dc)初始为(0,0),先沿着矩阵第一列移动(dr++),当到达第一列最下边的元素时，再沿着矩阵最后一行移动(dc++)
上坐标与下坐标同步移动，每次移动后，打印上坐标和下坐标的连线上的元素
如果上一次斜线从左下向右上打印，这次就从右上向左下打印，反之亦然
把打印的方向用 boolean 表示，每次取反
"""


def printMatrixZigZag(matrix):
    if not matrix or not matrix[0]:
        return None
    tr, tc, dr, dc = 0, 0, 0, 0
    endr, endc = len(matrix) - 1, len(matrix[0]) - 1
    fromUp = False
    tmp = []  # 装最终结果
    while tr <= endr:
        printLevel(matrix, tr, tc, dr, dc, fromUp, tmp)
        tr = tr + 1 if tc == endc else tr
        tc = tc if tc == endc else tc + 1
        dc = dc + 1 if dr == endr else dc
        dr = dr if dr == endr else dr + 1  # 注意顺序，dc的赋值应该在dr后面，反之出错
        fromUp = not fromUp
    print(tmp)

def printLevel(m, tr, tc, dr, dc, f, tmp):
    ans = []
    if f:
        while tr != dr + 1:
            ans.append(m[tr][tc])
            tr, tc = tr + 1, tc - 1
    else:
        while dr != tr - 1:
            ans.append(m[dr][dc])
            dr, dc = dr - 1, dc + 1
    tmp.extend(ans)


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]
    printMatrixZigZag(matrix)
