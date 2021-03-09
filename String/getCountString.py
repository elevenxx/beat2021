"""
给定一个字符串，返回统计字符串。
"""

def getCountString(s):
    if not s or s == "":
        return ""
    res = [s[0]]
    count = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            res.extend([str(count), s[i]])
            count = 1
        else:
            count += 1
    res.append(str(count))
    return ''.join(res)


if __name__ == "__main__":
    strs = "aaabbccccdddaffc"
    print(getCountString(strs))