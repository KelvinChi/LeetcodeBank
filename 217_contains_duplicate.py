#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def contains_duplicate(lis):
    temp = set(lis)
    print('True') if len(temp) != len(lis) else print('False')


a = [1, 1, 5, 6]
b = [1, 3, 5, 6]
contains_duplicate(a)
contains_duplicate(b)
