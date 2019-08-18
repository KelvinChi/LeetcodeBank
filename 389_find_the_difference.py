#!/usr/bin/env python
# -*- coding:utf8 -*-
# Created by CK 2019-04-30 04:35:40


def ftd(s, t):
    a = list(s)
    b = list(t)
    a.sort()
    b.sort()
    for i in b:
        if i not in a:
            print(i)


s = 'abcd'
t = 'abced'
ftd(s, t)
