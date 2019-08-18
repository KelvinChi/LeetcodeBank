#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def mccs(lis):
    i = -1
    step = 0
    while i < len(lis) - 2:
        step += min(lis[i + 1], lis[i + 2])
        i = i + 1 if lis[i + 1] < lis[i + 2] else i + 2
    return step


lis = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(mccs(lis))
