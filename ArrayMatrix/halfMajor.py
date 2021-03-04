"""
给一个数组，打印其中出现次数大于一半的数。
进阶：给一个数组arr和整数 k，打印所有出现次数大于 N/k的数。
思路：
candidate 方法，候选人。
每次在数组中删掉两个不同的数，cand为候选，times为次数
当times==0时，表示当前没有候选，则把当前数arr[i]设置为候选，同时times设置为 1.
当times!=0时，表示当前有候选，如果arr[i]==cand,则times++,否则times--.
最后检验剩下来的那个数是否真的出现次数大于一半。
扩展：
投票有效的条件是必须一个候选人得票数超过一半。但是验票人不知道每张选票选了谁，只能把任意两张选票放在机器上看这两张选票是否一样。
本体解法只需要对当前数和候选数做比较，不需要知道具体数值。
"""


def halfMajor(arr):
    cand = 0
    times = 0
    for i in range(len(arr)):
        if times == 0:
            cand = arr[i]
            times = 1
        elif arr[i] == cand:
            times += 1
        else:
            times -= 1

    times = 0
    for i in range(len(arr)):
        if arr[i] == cand:
            times += 1
    if times > len(arr) / 2:
        print(cand)
        #print(times)
    else:
        print("no such number")

if __name__ == "__main__":
    A = [3, 2, 3]
    #A = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    halfMajor(A)
    B = list(range(8))
    halfMajor(B)