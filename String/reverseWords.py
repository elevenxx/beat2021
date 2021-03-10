"""
给一个字符类型的数组，翻转字符串里的单词。
"""


# 使用内置函数
def reverseWords1(s):
    return " ".join(reversed(s.split()))


def reverseWords2(s):
    if not s or len(s) == 0:
        return
    s = [e for e in s]
    reverse(s, 0, len(s) - 1)

    l, r = 0, 0
    while l < len(s):
        # 找单词的末尾
        while r < len(s) and s[r] != ' ':
            r += 1
        # 翻转单词
        reverse(s, l, r - 1)
        # 更新左右指针
        l, r = r + 1, r + 1
    return s


def reverse(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1


def reverseWords3(s):
    res = ''
    i = 0
    while i < len(s):
        word = ''
        while i < len(s) and s[i] != ' ':
            word += s[i]
            i += 1
        i += 1
        if word:
            res = word + ' ' + res
    return res[:-1]


if __name__ == "__main__":
    s = "the sky is blue"
    t = "  hello world!  "
    #print(reverseWords1(t))
    #print(reverseWords2(t))
    print(reverseWords3(s))
