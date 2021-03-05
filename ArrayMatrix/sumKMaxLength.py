"""
给定一个无序数组arr，元素全为正数，一个数k，求arr的所有子数组中所有元素相加和为k的最长子数组长度。
思路：
双指针，left,right开始时都为0.
变量cur记录当前arr[left..right]的和(包括right位置元素)，初始值为arr[0]
变量ans记录累加和为k的所有子数组中最大子数组的长度，初始值为0.
当right到达数组末尾前，开始下面循环：
根据cur和k的大小比较决定指针移动：
1)cur==k,比较right-left+1与ans大小，若大于ans,则更新ans。
因为数组中元素均为正，从left开始到right位置之后的子数组均大于k。left--,cur-arr[left]
2)cur<k,right++,判断是否越界,cur+arr[right]
3)cur>k,cur-arr[left],left++
"""


def sumKfindMaxLength(arr, k):
    if not arr or len(arr) == 0 or k <= 0:
        return
    left, right = 0, 0
    cur = arr[0]
    ans = 0
    while right < len(arr):
        if cur == k:
            ans = max(ans, right-left+1)
            cur -= arr[left]
            left += 1
        elif cur < k:
            right += 1
            if right == len(arr):
                break
            cur += arr[right]
        else:
            cur -= arr[left]
            left += 1
    return ans


if __name__ == "__main__":
    A = [1, 2, 1, 1, 1, 4]
    print(sumKfindMaxLength(A, 3))