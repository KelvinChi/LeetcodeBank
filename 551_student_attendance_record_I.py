#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-22 09:21:01


def sari(string):
    for i in range(3, len(string)):
        if 'L' * i in string or string.count('A') >= 2:
            return False
    else:
        return True


string = 'PPALLP'
print(str(sari(string)))
string = 'PPALLL'
print(str(sari(string)))
