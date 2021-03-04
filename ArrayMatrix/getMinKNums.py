"""
给定一个无序数组，找到其中最小的 k 个数
要求时间复杂度 O(N)
思路：
借鉴快排思想，快排的划分 partition 函数每次执行完后都能将数组分成两个部分
小于等于分界值 pivot 的元素放在数组左边，大于它的元素放在右边，返回 pivot 在数组中的下标
与快排不同，这里只处理划分后的一边即可
定义函数 random_select(A, l, r, k)表示划分数组 A 的[l,r]部分，使前 k 小的元素在左侧
调用 partition 函数，假设返回的下标是 pos，即 pivot 在数组中的最终位置
pivot 是数组中第 pos-l+1 小的数
pos-l+1 == k: pivot 即为第 k 小的数
pos-l+1 < k: 第 k 小的数在 pivot 右边，递归调用 random_select(A, pos+1, r, k-(pos-l+1))
pos-l+1 > k: 第 k 小的数在 pivot 左边，递归调用 random_select(A, l, pos-1, k)
函数递归入口为 random_select(A, 0, len(A), k)
返回后前 k 个数即为答案
"""

import random

def partition(A, l, r):
    pivot = A[r]
    i = l - 1
    for j in range(l, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def random_partition(A, l, r):
    i = random.randint(l, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, l, r)

def random_select(A, l, r, k):
    pos = random_partition(A, l, r)
    num = pos - l + 1
    if k < num:
        random_select(A, l, pos-1, k)
    elif k > num:
        random_select(A, pos+1, r, k-num)

def getMinKNumbers(A, k):
    if k == 0:
        return None
    random_select(A, 0, len(A)-1, k)
    print(A[:k])


if __name__ == "__main__":
    nums = [1, 5, 3, 4, 2, 6, 7]
    getMinKNumbers(nums, 3)
