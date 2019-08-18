#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-29 01:16:11


def rtm(array, r, c):
    original_r = len(array)
    original_c = len(array[0])
    if r * c != original_r * original_c:
        print(array)
    else:
        temp = [(array[0] + x) for x in array[1:]][0]
        new_array = []
        for i in range(r):
            new_array.append(temp[c * i: c * i + c])
        print(new_array)


array = [[1, 2, 3, 4], [5, 6, 7, 8]]
r = 4
c = 2
rtm(array, r, c)
