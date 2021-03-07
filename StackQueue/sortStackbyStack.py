"""
对一个栈从顶到底按从大到小的顺序排序，要求只能申请一个额外的栈。
思路：
将要排序的栈记为 s,申请的辅助栈记为 help.
保证help从栈顶到栈底元素从小到大排序.
在 s 上执行 pop 操作，弹出元素记为 cur.
若 cur 大于 help 栈顶元素，则不断从 help 中弹出元素到s，直到cur小于等于help栈顶元素，将cur压入help.
若 cur 小于等于 help 栈顶元素，直接压入 help.
执行上述操作，直到 s 中全部元素都压入到 help，此时 help 从栈顶到栈顶元素为从小到大顺序.
最后将 help 元素全部压入 s，即为题目所求.
"""


def sortStackbyStack(s):
    help = []
    while s:
        cur = s.pop()
        while help and cur > help[-1]:
            s.append(help.pop())
        help.append(cur)

    while help:
        s.append(help.pop())
    return s


if __name__ == "__main__":
    s1 = [1, 2, 5, 6, 3, 4, 1, 2, 7, 1]
    print(sortStackbyStack(s1))
