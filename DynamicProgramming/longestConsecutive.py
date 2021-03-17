"""
给定无序数组arr，返回其中最长的连续序列的长度
思路：
哈希表 dic,key代表遍历过的某个数，value代表key所在的最长连续序列的长度
遍历数组arr，如果arr[i]之前出现过，直接遍历下一个数
如果arr[i]没有出现过，那么加入dic里，dic[arr[i]]=1
查看arr[i]-1是否在dic里，如果在，则说明arr[i]-1所在的连续序列可以和arr[i]合并，合并后记为A序列。
记序列中最小值为leftA,最大值为rightA,更新dic中leftA,rightA的记录为(leftA,lenA),(rightA,lenA)
同样查看arr[i]+1是否在dic里。
ans记录每次合并后的序列的长度最大值。
备注：
因为每次只处理之前没有更新过的数字。
如果一个新的数字能够把某个连续空间扩大，或把某两个连续区间连在一起，那么
只需要有这个区间的最大值和最小值即可，中间的数不会用到，所以只更新最大最小值在dic中的记录。
"""

def longestConsecutive(arr):
    if not arr or len(arr) == 0:
        return 0
    ans = 1
    dic = {}
    for e in arr:
        if e not in dic:
            dic[e] = 1
            # 下面两个if都应该在上面的if嵌套下进行，否则会重复计算长度
            if e-1 in dic:
                ans = max(ans, merge(dic, e-1, e))
            if e+1 in dic:
                ans = max(ans, merge(dic, e, e+1))
    return ans

def merge(dic, less, more):
    left = less - dic[less] + 1
    right = more + dic[more] - 1
    lens = right - left + 1
    dic[left] = lens
    dic[right] = lens
    return lens


if __name__ == "__main__":
    arr = [100,4,200,1,3,2,4]
    print(longestConsecutive(arr))