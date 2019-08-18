#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-20 02:32:31


def lkf(s, a):
    num = s.count('-')
    lis = list(s)
    for i in range(num):
        lis.remove('-')
    lis = list(''.join(lis).upper())
    if len(lis) % 4 == 0:
        num1 = len(lis) / 4 - 1
    else:
        num1 = len(lis) // 4
    for i in range(int(num1)):
        lis.insert(-(i + 1) * 4 - i, '-')
    return ''.join(lis)


s = '5F3Z-2e-9-w5we54815151kdfalsdkfj8'
a = 4
print(lkf(s, a))
