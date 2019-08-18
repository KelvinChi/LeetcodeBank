#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-20 01:54:50


def heaters(lis):
    temp = (lis[0] + lis[-1]) / 2
    for i in range(len(lis)):
        if lis[i] <= temp and lis[i + 1] >= temp:
            print(lis[i + 1] - lis[0]) if lis[-1] - lis[i] >= lis[i + 1] - lis[0] \
                else print(lis[-1] - lis[i])


lis = [1, 3, 5, 9, 13, 15]
heaters(lis)
