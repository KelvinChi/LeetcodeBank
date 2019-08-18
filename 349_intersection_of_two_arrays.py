#!/usr/bin/env python
# -*- coding:utf8 -*-
# Created by CK 2019-04-28 08:01:34


def choose(lis1, lis2):
    return (lis1, lis2) if len(lis1) < len(lis2) else (lis2, lis1)


def intersection_of_two_arrays(lis1, lis2):
    temp = choose(lis1, lis2)
    result = []
    for i in temp[0]:
        if i in temp[1]:
            result.append(i)
    return list(set(result))


a = [4, 9, 5]
b = [9, 4, 9, 8, 4]
print(intersection_of_two_arrays(a, b))
