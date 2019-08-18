#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-11 03:16:13


def output_alpha(num):
    if 0 < num < 9:
        return str(num)
    dic = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    for key, value in dic.items():
        if num == key:
            return value


def get_num(num):
    global result
    a = abs(num)
    b = a // 16
    c = a % 16
    result.insert(0, output_alpha(c))
    if b > 15:
        get_num(b)
    else:
        result.insert(0, output_alpha(b))
    return result


def canth(num):
    if num == 0:
        return '0'
    elif num > 0:
        return ''.join(get_num(num))
    elif num < 0:
        a = get_num(num)
        a.insert(0, '-')
        return ''.join(a)


result = []
b = -860988
print(hex(b))
print(canth(b))
