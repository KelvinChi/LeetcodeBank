#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-17 01:31:55


def faaias(string, keyalpha):
    length = len(keyalpha)
    for i in range(len(string) - 1):
        if ''.join(sorted(string[i: i + length])) ==\
                ''.join(sorted(keyalpha)):
            print(i)


a = 'cbaebabacd'
b = 'abc'
faaias(a, b)
