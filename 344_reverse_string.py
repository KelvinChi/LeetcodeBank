#!/usr/bin/env python
# -*- coding:utf8 -*-
# Created by CK 2019-04-28 04:59:14


import copy


def char(word):
    lis = list(word)
    temp = copy.deepcopy(lis)
    for i in range(len(lis)):
        lis[i] = temp[-i - 1]
    return lis


word = 'Hello'
print(char(word))
