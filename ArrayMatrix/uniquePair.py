"""
给定排序数组arr和整数k，不重复打印arr中相加和为k的不降序二元组。
拓展:
不重复打印arr中相加和为k的不降序三元组。
思路：
利用排序数组特点，用双指针。左右指针刚开始指向数组开头和结尾元素。
左、右指针不断向中间压缩，直至相遇。
1) arr[left] + arr[right] == k: 打印,left++,right--
2) > k: right--
3) < k: left++
要保证不重复，在打印时增加一个检查，检查arr[left]与arr[left-1]是否相等。
若相等，则跳过，因为之前肯定打印过了。
时间复杂度 O(N)
"""


def uniquePair(arr, k):
    if not arr or len(arr) < 2:
        return
    ans = []
    left, right = 0, len(arr)-1
    while left < right:
        if arr[left] + arr[right] < k:
            left += 1
        elif arr[left] + arr[right] > k:
            right -= 1
        else:
            if left == 0 or arr[left] != arr[left-1]:
                ans.append((arr[left], arr[right]))
            left += 1
            right -= 1
    return ans


if __name__ == "__main__":
    A = [-8, -4, -3, 0, 1, 2, 4, 5, 8, 9]
    print(uniquePair(A, 10))

