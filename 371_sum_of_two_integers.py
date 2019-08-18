#!/usr/bin/env python
# -*- coding:utf8 -*-
# Created by CK 2019-04-29 08:22:50


def add_fun(a, b):
    temp = [a, b]
    return sum(temp)


a = 1
b = 2
print(add_fun(a, b))
a = -1
b = 2
print(add_fun(a, b))
