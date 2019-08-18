#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def mtsl(l1, l2):
    l1.extend(l2)
    l1.sort()
    return l1


a = [1, 4, 6]
b = [1, 3, 6]
c = mtsl(a, b)
print(c)
