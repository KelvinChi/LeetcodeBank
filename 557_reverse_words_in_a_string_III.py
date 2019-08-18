#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-22 12:28:04


def rwiasiii(string):
    lis = string.split(' ')
    for i in range(len(lis)):
        lis[i] = ''.join(list(reversed(lis[i])))
        if i > 0:
            lis.insert(2 * i - 1, ' ')
    print(''.join(lis))


string = "Let's take this"
rwiasiii(string)
