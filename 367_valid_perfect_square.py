#!/usr/bin/env python
# -*- coding:utf8 -*-
# Created by CK 2019-04-28 08:53:16


def check(num):
    temp = 1
    squr = 0
    while True:
        if squr < num:
            temp += 1
            squr = temp ** 2
        elif squr > num:
            print('False')
            break
        else:
            print('True')
            break


a = 16
check(a)
b = 14
check(b)
