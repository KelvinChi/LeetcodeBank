#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-11 04:20:27


def tmn(lis):
    a = sorted(list(set(lis)))
    return a[-1] if len(a) < 3 else a[0]


lis = [2, 2, 3, 1]
print(tmn(lis))
