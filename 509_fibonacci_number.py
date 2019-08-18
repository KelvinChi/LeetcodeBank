#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-21 01:45:15


def fn(num):
    a = b = 1
    if num == 1 or num == 2:
        return 1
    else:
        for i in range(num - 2):
            a, b = b, a + b
    return b


num = 100
for i in range(1, num):
    print(fn(i), end=' ')
    if i % 10 == 0:
        print('\n')
