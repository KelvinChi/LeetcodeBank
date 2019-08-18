#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-20 02:49:01


def mco(lis):
    count = 0
    temp = 0
    for i in lis:
        if i == 1:
            temp += 1
        elif i == 0:
            if temp > count:
                count = temp
            temp = 0
    return count


lis = [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0]
print(mco(lis))
