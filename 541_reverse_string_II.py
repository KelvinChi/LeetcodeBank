#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-22 07:16:19


def rsii(lis, k):
    lis = list(lis)
    temp = []
    a = len(lis) // (2 * k)
    b = len(lis) % (2 * k)
    for i in range(a):
        c = reversed(lis[k*i: k*i + k])
        temp.extend(c)
        d = lis[k * i + k: k * i + (2 * k)]
        temp.extend(d)
    if b <= k:
        e = reversed(lis[-b:])
        temp.extend(e)
    else:
        e = reversed(lis[-b: -b + k])
        temp.extend(e)
        f = lis[-b + k:]
        temp.extend(f)
    return ''.join(temp)


lis = 'abcdefg'
k = 2
print(rsii(lis, k))
