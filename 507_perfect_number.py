#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-20 08:14:38


def pn(num):
    lis = []
    for i in range(1, num):
        if num % i == 0:
            lis.append(i)
    if sum(lis) == num:
        return num
    else:
        return 0


for i in range(1, 10000):
    if pn(i) != 0:
        print(pn(i))
