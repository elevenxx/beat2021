"""
给定一个字符串数组，将字母异位词组合在一起。
"""
from collections import defaultdict

def groupAnagrams(strs):
    dic = defaultdict(list)
    for st in strs:
        count = [0] * 26
        for ch in st:
            count[ord(ch) - ord('a')] += 1
        # 将list类型转为tuple进行哈希
        dic[tuple(count)].append(st)
    return list(dic.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))