#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def valid_anagram(s, t):
    a = sorted(list(s))
    b = sorted(list(t))
    if a == b:
        print('True')
    else:
        print('False')


s = 'anagram'
t = 'nagaram'
valid_anagram(s, t)

