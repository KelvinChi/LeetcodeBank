#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def get_input():
    a = input('请输入第一个数')
    b = input('请输入第二个数')
    print('参考结果：' + str(int(a) + int(b)))
    if len(a) < len(b):
        pass
    else:
        c = a
        a = b
        b = c
    return a, b


class Solution:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def _get_num(self, num):
        temp = []
        ls = list(num)
        for i in range(len(num)):
            temp.append(ls.pop())
        return temp

    def result(self):
        l1 = self._get_num(self.n1)
        # 在数字列表1末尾加‘0’*some
        for h in range((len(self.n2) - len(self.n1) + 1)):
            l1.append('0')
        l2 = self._get_num(self.n2)
        # 在数字列表2后加1个‘0’
        l2.append('0')
        r_n = []
        guide = len(self.n2)
        for j in range(guide):
            nj1 = int(l1[j])
            nj2 = int(l2[j])
            leave_num = (nj1 + nj2) % 10
            carry_num = (nj1 + nj2) // 10
            l1[j + 1] = int(l1[j + 1]) + carry_num
            r_n.append(str(leave_num))
        if int(l1[guide]) + int(l2[guide]) == 0:
            pass
        else:
            r_n.append(str(int(l1[guide]) + int(l2[guide])))
        result_num = ''.join(list(reversed(r_n)))
        return result_num


def main():
    a = get_input()
    b = Solution(a[0], a[1])
    print('结果为：' + b.result())


if __name__ == '__main__':
    main()
