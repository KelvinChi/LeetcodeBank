#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-20 02:54:05


def ctr(num):
    temp = int(num ** 0.5)
    for i in range(temp, 0, -1):
        if num % i == 0:
            width = i
            length = int(num / i)
            break
    return length, width


num = 6
print(ctr(num))
