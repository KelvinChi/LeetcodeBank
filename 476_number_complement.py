#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-20 02:18:01


def nc(num):
    temp = list(bin(num))
    lis = []
    if temp[0] == '-':
        lis.append('-')
        temp = temp[3:]
    else:
        temp = temp[2:]
    for i in temp:
        if i == '1':
            lis.append('0')
        elif i == '0':
            lis.append('1')
    result = int(''.join(lis), 2)
    print(result)


num = -5
nc(num)
