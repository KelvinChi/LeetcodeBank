#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-17 03:08:29


def sc(string):
    a = sorted(list(set(string)))
    lis = []
    count = 0
    for i in a:
        b = string.count(i)
        if b != 1:
            lis.append(b)
    for j in lis:
        count += len(str(j))
    print(count + len(a))


string = ["a", "a", "b", "b", "c", "c", "c"]
sc(string)
a = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
sc(a)
