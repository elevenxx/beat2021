"""
实现一个栈，返回栈中最小元素。要求pop,push,getMin操作的时间复杂度为O(1).
思路：
使用两个栈，一个栈stackData用来保存元素，
一个栈stackMin用来保存每一步的最小值。
操作：
1)压入数据：
直接压入stackData。判断stackMin是否为空，若为空，直接压入；
不为空，比较当前元素和栈顶元素大小，若当前元素更小，直接压入，反之不进行操作。
2)弹出数据：
stackData弹出栈顶元素e，比较e与stackMin栈顶元素大小。
因为stackMin保存每一步最小值，所以栈顶元素只可能小于等于e。
当栈顶元素小于e，不进行操作。
当栈顶元素等于e，弹出。弹出操作与压入操作是对应的。
3)查询最小值操作：
直接返回stackMin栈顶元素即可。
"""


class MyStacktoGetMin:
    def __init__(self):
        self.stackData = []
        self.stackMin = []

    def push(self, x):
        self.stackData.append(x)
        if not self.stackMin or self.stackMin[-1] > x:
            self.stackMin.append(x)

    def pop(self):
        e = self.stackData.pop()
        if self.stackMin[-1] == e:
            self.stackMin.pop()

    def getMin(self):
        return self.stackMin[-1]


if __name__ == "__main__":
    obj = MyStacktoGetMin()
    obj.push(1)
    obj.push(2)
    print(obj.getMin())