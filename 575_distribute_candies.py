#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-29 05:23:11


def dc(lis):
    return min(len(lis) / 2, len(list(set(lis))))


a = [1, 1, 2, 2, 3, 3]
print(dc(a))
b = [1, 1, 2, 3]
print(dc(b))
