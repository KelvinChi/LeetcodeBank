#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def pt(n):
    temp = [1, 1]
    b = 3 * n
    if n == 1:
        a = ' 1 '
        print(a.center(b))
    elif n == 2:
        a = ' 1 1 '
        print(a.center(b))
    else:
        for i in range(3, n + 1):
            ln = [0] * i
            # print(i)
            # print(ln)
            for j in range(1, i //2 + 1):
                ln[0] = ln[i - 1] = 1
                ln[j] = temp[j - 1] + temp[j]
                ln[i - 1 -j] = ln[j]
            temp = ln
            a = ' '
            for l in ln:
                a += (str(l) + ' ')
        print(ln)

pt(10)