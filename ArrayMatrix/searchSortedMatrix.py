"""
给定一个NxM矩阵，一个数K，矩阵每行有序，每列有序，判断K是否在矩阵中。
思路：
从右上角或者左下角开始查找，时间复杂度O(N+M)
从右上角开始，比较当前数与K的大小
1)若比K大，说明当前列下方的数都比K大，应该向左走，col--
2)若比K小，说明当前行左边的数都比K小，应该向下走，row++
如果找到越界都没有与K相等的数，返回False
"""

def searchMatrix(M, K):
    row, col = 0, len(M[0])-1
    while row < len(M) and col >= 0:
        if M[row][col] == K:
            return True
        elif M[row][col] > K:
            col -= 1
        else:
            row += 1

    return False

if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    print(searchMatrix(matrix, 12))
    print(searchMatrix(matrix, 0))
    print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))