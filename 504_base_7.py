#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-20 07:26:06


def base7(num):
    temp = abs(num)
    quotient = temp // 7
    remainder = temp % 7
    result = [str(remainder)]
    while quotient > 7:
        remainder = quotient % 7
        result.insert(0, str(remainder))
        quotient //= 7
    result.insert(0, str(quotient))
    if num < 0:
        result.insert(0, '-')
    return int(''.join(result))


num = 100
print(base7(num))
