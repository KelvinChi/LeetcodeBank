#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-11 04:14:44


def judge(num):
    a = num % 3
    b = num % 5
    if a == 0 and b != 0:
        return 'Fizz'
    elif a != 0 and b == 0:
        return 'Buzz'
    elif a == 0 and b == 0:
        return 'FizzBuzz'
    else:
        return str(num)


def fb(num):
    result = []
    for i in range(1, num + 1):
        result.append(judge(i))
    return result


print(fb(15))
