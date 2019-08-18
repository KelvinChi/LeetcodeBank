#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-17 09:08:54


import pysnooper


@pysnooper.snoop()
def hd(x, y):
    count = 0
    a = list(bin(x))[2:]
    b = list(bin(y))[2:]
    c = max(len(a), len(b))
    if len(a) < c:
        for i in range(c - len(a)):
            a.insert(0, '0')
    if len(b) < c:
        for i in range(c - len(b)):
            b.insert(0, '0')
    for i in range(c):
        if a[i] != b[i]:
            count += 1
    return count


x = 115151
y = 4668
print(hd(x, y))
