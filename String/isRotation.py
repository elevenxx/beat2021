"""
判断两个字符串是否互为旋转词。
思路：
首先判断长度。
string a, string b
生成b2=b+b，判断a是否在b2里面。
若在，则为旋转词。因为b2里面包括b的所有旋转词。
"""

def isRotation(A, B):
    if len(A) != len(B):
        return False
    B2 = B + B
    return (A in B2)


if __name__ == "__main__":
    A = 'abcde'
    #B = 'cdeab'
    B = 'cdeaC'
    print(isRotation(A, B))