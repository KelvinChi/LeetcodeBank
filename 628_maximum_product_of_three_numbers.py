#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-31 03:31:02


def mpotn(lis):
    lis.sort()
    result = 1
    for i in lis[-3:]:
        result *= i
    return result


lis = [1, 3, 2, 5, 8]
print(mpotn(lis))
