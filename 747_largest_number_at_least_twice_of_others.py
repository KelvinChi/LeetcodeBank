#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def lnaltoo(lis):
    biggest = max(lis)
    ind = lis.index(biggest)
    lis.pop(ind)
    for i in lis:
        if 2 * i > biggest:
            return -1
    else:
        return ind


lis = [3, 6, 1, 0]
lis1 = [1, 2, 3, 4]
print(lnaltoo(lis))
print(lnaltoo(lis1))