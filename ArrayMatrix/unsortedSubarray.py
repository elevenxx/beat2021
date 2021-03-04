"""
给定一个无序数组，求出需要排序的最短子数组的长度。
思路：
两个变量 left，right 分别记录最左边和最右边逆序出现的位置
初始化 left = -1，从右向左遍历，遍历的过程中记录右侧出现的数的最小值，记为 minR.
假设当前数为 arr[i],如果 arr[i]>minR，说明如果整体有序，arr[i]应该在 minR 右边。
left 记录最左边出现这样情况的位置。若遍历完成，left=-1说明整体有序，无需排序。
接下来从左到右排序，遍历过程中记录左侧出现的数的最大值，记为 maxL.
假设当前数为 arr[i],如果 arr[i]<maxL，说明如果整体有序，arr[i]应该在 maxL 左边。
right 记录最右边出现这样情况的位置。
遍历完成后，arr[left..right]是真正需要排序的部分，返回长度即可。
"""


def findUnsortedSubarray(arr):
    if not arr or len(arr) < 2:
        return 0
    left = -1
    minR = arr[-1]
    for i in range(len(arr)-2, -1 , -1):
        if arr[i] > minR:
            left = i
        else:
            minR = min(minR, arr[i])
    if left == -1:
        return 0
    right = -1
    maxL = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < maxL:
            right = i
        else:
            maxL = max(maxL, arr[i])
    print(right - left + 1)


if __name__ == "__main__":
    A = [1, 5, 3, 4, 2, 6, 7]
    findUnsortedSubarray(A)