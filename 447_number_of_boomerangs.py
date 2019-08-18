#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-17 06:28:25


def judge1(key1, key2):
    a = list(key1)
    b = list(key2)
    a.extend(b)
    result = len(set(a))
    return True if result == 3 else False


def judge2(dic):
    a, b = list(dic.keys()), list(dic.values())
    count = 0
    result = 0
    while count < len(b) - 1:
        for i in range(len(b) - count - 1):
            if b[count] == b[i + count + 1]:
                if judge1(a[count], a[i + count + 1]):
                    result += 1
        count += 1
    return result * 2


def nob(lis):
    dic = {}
    count = 0
    while count < len(lis) - 1:
        for i in range(len(lis) - count - 1):
            dic[(count, i + count + 1)] = \
                (lis[count][0] - lis[i + count + 1][0]) ** 2 + \
                (lis[count][1] - lis[i + count + 1][1]) ** 2
        count += 1
    return dic


lis = [[0, 0], [1, 0], [2, 0]]
a = nob(lis)
print(judge2(a))
