#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-29 06:24:06


def lhs(lis):
    temp = list(sorted(set(lis)))
    count = []
    result = 0
    for i in temp:
        count.append(lis.count(i))
    for i in range(len(count) - 1):
        if result < count[i] + count[i + 1]:
            result = count[i] + count[i + 1]
    return result


lis = [1, 3, 2, 2, 5, 2, 3, 7]
print(lhs(lis))
