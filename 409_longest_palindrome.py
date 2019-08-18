#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-11 04:02:13


def lp(string):
    a = set(string)
    d = 0
    e = 0
    for i in a:
        b = string.count(i)
        if judge(b):
            d += b
        else:
            e += 1
    if e == 0:
        return d
    else:
        return d + 1


def judge(num):
    if num % 2 == 0:
        return True


a = 'abccccdd'
print(lp(a))
