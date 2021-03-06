"""
给定一个数组arr，将这个数组看作一个容器，返回容器能装多少水。
思路：
每次到达数组的第i位置，单独考虑i位置上方能有几格水。
双指针，left,right，初始值分别设为1，len(arr)-2
两个变量h1,h2
h1代表arr[0..left-1]中最大值,初始值arr[0]
h2代表arr[right..len(arr)-1]中最大值，初始值arr[-1]
当遍历到达数组的第i位置，i位置上方的水取决于最左边/最右边最高高度的较小值。
比如当h1<h2时，left右侧，right左侧还有未遍历的区域，该区域高度最大值可能比h2大。此时限制装水的即为h1。
"""

def getMaxWater(arr):
    if not arr or len(arr) < 3:
        return 0
    ans = 0
    left, right = 1, len(arr) - 2
    h1, h2 = arr[0], arr[-1]
    while left <= right:
        if h1 <= h2:
            ans += max(0, h1 - arr[left])
            h1 = max(h1, arr[left])
            left += 1
        else:
            ans += max(0, h2 - arr[right])
            h2 = max(h2, arr[right])
            right -= 1
    return ans


if __name__ == "__main__":
    #A = [3,1,2,5,2,4]
    A = [4,5,1,3,2]
    print(getMaxWater(A))