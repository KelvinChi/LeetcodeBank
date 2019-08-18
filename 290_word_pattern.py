#!/usr/bin/env python
# -*- coding:utf8 -*-
# Created by CK 2019-04-26 07:15:03


def get_set(lis):
    temp = []
    for i in range(len(lis)):
        if lis[i] not in temp:
            temp.append(lis[i])
    return temp


def word_pattern(pattern, string):
    temp = string.split(' ')
    temp_set = get_set(temp)
    pattern_set = get_set(pattern)
    pin = 0
    if len(temp_set) != len(pattern_set):
        print('False')
    else:
        for i in range(len(pattern)):
            if temp_set.index(temp[i]) != pattern_set.index(pattern[i]):
                print('False')
                return None
            else:
                pin += 1
        if pin == len(temp):
            print('True')


pattern = 'abba'
string = 'dog cat cat dog'
word_pattern(pattern, string)

pattern = 'abbb'
string = 'dog cat cat fish'
word_pattern(pattern, string)

pattern = 'aaaa'
string = 'dog cat cat dog'
word_pattern(pattern, string)
