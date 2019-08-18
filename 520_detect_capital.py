#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-21 02:05:47


def dc(string):
    if string.lower() == string \
            or string.upper() == string \
            or string.lower().title() == string:
        return True
    else:
        return False


s1 = 'USA'
s2 = 'China'
s3 = 'HaHa'
print(str(dc(s1)))
print(str(dc(s2)))
print(str(dc(s3)))
