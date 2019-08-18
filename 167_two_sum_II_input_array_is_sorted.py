#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def two_sum(lis, target):
    for i in lis:
        if i < target:
            c = target - i
            if i != c and c in lis:
                b = lis.index(i)
                d = lis.index(c)
                print(b, d)
                return
    print('None')


a = [2, 7, 11, 15]
target = 23
two_sum(a, target)