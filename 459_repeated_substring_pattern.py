#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-17 08:34:41


def rsp(string):
    temp = 0
    while temp < len(string):
        try:
            temp += string[temp + 1:].index(string[0]) + 1
        except ValueError:
            return False
        if len(string) % temp == 0:
            if string[0: temp] * (len(string) // temp) == string:
                return True
    else:
        return False


string = 'abaaabaaabaaabaa'
print(rsp(string))
