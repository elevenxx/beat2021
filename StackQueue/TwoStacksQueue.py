"""
用两个栈实现队列，支持队列基本操作：add,poll,peek
思路：
两个栈，一个栈作为压入数据的栈sPush，一个作为弹出数据的栈sPop。
sPush只用来装数据，sPop只用来弹出数据。
注意：
在sPush往sPop压入数据时，sPop必须为空，必须一次性将sPush所有数据压入。
"""


class TwoStacksQueue:
    def __init__(self):
        self.sPush = []
        self.sPop = []

    # sPush往sPop压入数据
    def pushToPop(self):
        if not self.sPop:
            while self.sPush:
                self.sPop.append(self.sPush.pop())

    def add(self, x):
        self.sPush.append(x)
        self.pushToPop()

    def poll(self):
        self.pushToPop()
        return self.sPop.pop()

    def peek(self):
        self.pushToPop()
        return self.sPop[-1]


if __name__ == "__main__":
    q = TwoStacksQueue()
    q.add(1)
    q.add(3)
    q.add(2)
    print(q.poll())
    print(q.peek())