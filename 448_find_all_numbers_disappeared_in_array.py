#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-17 07:56:53


def fandia(lis):
    minimal = min(lis)
    maximal = max(lis)
    result = []
    for i in range(minimal, maximal + 1):
        if i not in lis:
            result.append(i)
    return result


lis = [4, 3, 2, 7, 8, 2, 3, 1]
print(fandia(lis))
