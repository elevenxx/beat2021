"""
给一个整型数组arr，大小为w的窗口从数组最左边滑到最右边，窗口每次向右滑一个位置。
返回 n-w+1 个窗口的最大值数组。
思路：
使用双端队列 q，q 存放数组 arr 的下标。
保持 q 中元素对应的 arr 数组元素从大到小排列。
q的压入规则：(只从队尾压入)
遍历数组，当前位置为 i, 元素为 arr[i]
1) q 为空，直接放入 i
2) q 不为空，q 队尾元素记为 j
若arr[j] > arr[i],那么把 i 放入 q 队尾
若arr[j] <= arr[i],那么不断弹出队尾元素，直到arr[q队尾元素] > arr[i]，再把i放入q队尾。
q的弹出规则：(只从队头弹出)
如果队头元素q[0]==i-w，说明已过期，滑动窗口已经移走，弹出队头元素。
"""


from collections import deque
def maxSlidingWindow(arr, w):
    if not arr or w < 1 or len(arr) < w:
        return None
    q = deque()
    res = []
    for i in range(len(arr)):
        while q and arr[q[-1]] <= arr[i]:
            q.pop()
        q.append(i)
        if q[0] == i - w:
            q.popleft()
        if i >= w - 1:
            res.append(arr[q[0]])
    return res


if __name__ == "__main__":
    A = [4, 3, 5, 4, 3, 3, 6, 7]
    print(maxSlidingWindow(A, 3))
    print(maxSlidingWindow(A, 4))
