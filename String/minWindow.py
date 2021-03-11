"""
给定字符串s,t，求s的子串中含有t所有字符的最小字串长度。
思路：
滑动窗口
i,j表示滑动窗口左、右边界
当这个窗口包含t所有字符，记录这个窗口的长度j-i+1，取所有窗口的最小值即可。
1)不断增加j使滑动窗口增大，直到窗口包含t所有字符。
2)不断增加i使窗口减小，排除不必要的元素，直到碰到一个必须包含的元素，记录此时窗口长度。
3)i++,此时窗口不满足条件，继续从1)开始，寻找新的满足条件的窗口，直到j到达字符串末尾。
用哈希表need记录当前滑动窗口还需要元素及其数量，变量needCnt记录还需要的元素的总数量。
need中元素对应的值若为负数，说明该元素多余。正数说明缺少。正好为零说明刚刚好。
needCnt是用来优化的，如果每次都要判断need中所有元素数量是否小于等于零，需要O(len(need))的时间复杂度，
needCnt记录当前所需元素总数量，当碰到一个所需元素，就needCnt--,为零说明窗口满足条件。时间复杂度降到O(1).
"""

from collections import Counter


def minWindow(s, t):
    #need = defaultdict(int)
    #for c in t:
    #    need[c] += 1
    need = Counter(t)
    needCnt = len(t)

    i = 0
    res = (0, float('inf'))
    for j, c in enumerate(s):
        if need[c] > 0:     # 这一步判断当前字符c是否是需要的，如果需要那么needCnt--
            needCnt -= 1
        need[c] -= 1
        if needCnt == 0:   # 当前滑动窗口满足条件，包含t所有字符
            while True:    # 尝试增大i
                cur = s[i]
                if need[cur] == 0:   # 这一步判断当前元素是否必须在滑动窗口，如果不在则导致窗口不满足条件
                    break
                need[cur] += 1
                i += 1

            if j - i < res[1] - res[0]:  # 记录结果
                res = (i, j)

            need[s[i]] += 1             # i++,寻找新的窗口
            needCnt += 1
            i += 1

    if res[1] > len(s):    # s中不包含t
        return 'no match'
    else:
        return s[res[0]:res[1]+1]



if __name__ == "__main__":
    s = 'abcde'
    t = 'ac'
    s1 = '12345'
    s2 = '35'
    print(minWindow(s, t))
    print(minWindow(s1, s2))
