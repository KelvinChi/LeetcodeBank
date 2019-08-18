#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def pt(n):
    temp = [1, 1]
    b = 3 * n
    for i in range(1, n + 1):
        if i == 1:
            a = ' 1 '
            print(a.center(b))
        elif i == 2:
            temp = [1, 1]
            a = ' 1 1 '
            print(a.center(b))
        else:
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
            print(a.center(b))

pt(10)