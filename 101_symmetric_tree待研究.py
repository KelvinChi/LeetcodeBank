#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def add_2(n):
    a = [1] * n
    a.reverse()
    print(list(reversed(a)))
    for i in range(1, 2 ** n):
        a[0] += 1
        for i in range(1, n):
            if a[i - 1] > 2:
                a[i] += 1
                a[i - 1] = 1
        print(list(reversed(a)))


add_2(5)
