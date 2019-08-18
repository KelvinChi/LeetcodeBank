#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-28 06:49:06


def api(lis):
    lis.sort()
    temp = []
    for i in range(0, len(lis), 2):
        temp.append(min(lis[i], lis[i + 1]))
    return sum(temp)


lis = [1, 4, 2, 3]
print(api(lis))
