#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-22 02:50:25


def lusi(string1, string2):
    return len(string1) if string1 == string2 else -1


s1 = 'abc'
s2 = 'abc'
print(lusi(s1, s2))
