#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-29 05:37:12


def sucs(lis):
    temp = sorted(lis)
    index_lis = []
    for i in range(len(lis)):
        if lis[i] != temp[i]:
            index_lis.append(i)
    if lis[:index_lis[0]] + sorted(lis[index_lis[0]:index_lis[-1] + 1]) \
            + lis[index_lis[-1] + 1:] == temp:
        print(len(index_lis))
    else:
        print('False')


lis = [2, 6, 4, 8, 10, 9, 15]
sucs(lis)
