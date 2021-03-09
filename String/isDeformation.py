"""
判断两个字符串是否互为变形词。
思路：
首先判断长度。长度不同直接返回FALSE
申请一个数组map，map[a]=b代表字符编码为a的字符出现了b次。
遍历字符串1后map数组就成为统计字符串1中每种字符的词频统计表。
遍历字符串2，每遍历到一个字符对应频数减一。
最后数组中每个元素都为零则代表两个字符串互为变形词。
"""

def isDeformation(s, t):
    if len(s) != len(t):
        return False
    dic = [0] * 26 # 假设只有小写字母
    for e in s:
        dic[ord(e) - ord('a')] += 1
    for e in t:
        if dic[ord(e) - ord('a')] <= 0:
            return False
        dic[ord(e) - ord('a')] -= 1
    return True


if __name__ == "__main__":
    s = "anagram"
    #t = "nagaram"
    t = "nagaramm"
    print(isDeformation(s, t))