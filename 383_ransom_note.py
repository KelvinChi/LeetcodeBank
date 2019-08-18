#!/usr/bin/env python
# -*- coding:utf8 -*-
# Created by CK 2019-04-29 08:39:20


def canConstruct(ransom, magazine):
    num = 0
    for i in list(set(ransom)):
        if i not in list(set(magazine)):
            print('i am the 1st false')
            break
        elif ransom.count(i) > magazine.count(i):
            print('i am the 22nd false')
            break
        else:
            num += 1
    if num == len(list(set(ransom))):
        print('true')


ransom = 'a'
magazine = 'b'
canConstruct(ransom, magazine)
ransom = 'aa'
magazine = 'ab'
canConstruct(ransom, magazine)
ransom = 'aa'
magazine = 'aab'
canConstruct(ransom, magazine)
