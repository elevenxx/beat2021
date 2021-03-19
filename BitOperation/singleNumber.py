"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
"""

def singleNum(arr):
    e = arr[0]
    for n in arr[1:]:
        e ^= n
    return e


if __name__ == "__main__":
    print(singleNum([1,2,3,2,1,3,5]))