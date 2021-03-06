"""
给定一个环路，上面有N个加油站，其中第i个加油站有汽油gas[i]升。
有一辆油箱容量无限的汽车，从第i个加油站开往第i+1个加油站需要消耗汽油cost[i]升。
从其中一个加油站出发，开始时油箱为空。
如果可以绕环路行驶一周，则返回出发时加油站的编号。
思路：
遍历数组
curr表示当前油量
"""

def gasStation(gas, cost):
    n = len(gas)
    if sum(gas) < sum(cost):
        return -1
    curr = 0
    pos = 0
    for i in range(n):
        curr += gas[i] - cost[i]
        if curr < 0:
            pos = i+1
            curr = 0
    return pos


if __name__ == "__main__":
    #gas = [1, 2, 3, 4, 5]
    #cost = [3, 4, 5, 1, 2]
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    print(gasStation(gas, cost))