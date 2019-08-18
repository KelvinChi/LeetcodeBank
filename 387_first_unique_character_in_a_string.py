#!/usr/bin/env python
# -*- coding:utf8 -*-
# Created by CK 2019-04-30 04:16:50


def fucias(string):
    new_string_list = []
    count = 0
    for i in string:
        if i not in new_string_list:
            new_string_list.append(i)
    for i in new_string_list:
        if string.count(i) % 2 != 0:
            return string.index(i)
        else:
            count += 1
    if count == len(new_string_list):
        return -1


s = 'leetcode'
print(fucias(s))
s = 'loveleetcode'
print(fucias(s))
