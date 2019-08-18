#!/usr/bin/env python
# -*- coding:utf8 -*-
# Created by CK 2019-04-12 06:47:00


import random


def generation(s, e):
    a = random.randint(1, e)
    return a


def judge(s, e):
    if e - s == 1:
        print('%d is the first nok version' % s) if s in noklist else print('%d is the first nok version' % e)
    else:
        temp = s + ((e - s) // 2)
        judge(temp, e) if temp in oklist else judge(s, temp)


if __name__ == '__main__':
    s = 1
    e = 30
    a = generation(s, e)
    oklist = range(s, a)
    noklist = range(a, e)
    judge(s, e)
