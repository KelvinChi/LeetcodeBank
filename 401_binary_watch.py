#!/usr/bin/env python
# -*- coding:utf8 -*-
# Created by CK 2019-04-30 07:14:48


def hour(h):
    if h == 1:
        result = [1, 2, 4, 8]
    elif h == 2:
        result = [3, 5, 6, 9, 10, 12]
    elif h == 3:
        result = [7, 11]
    return result


def minute(m):
    if m == 1:
        result = [1, 2, 4, 8, 16, 32]
    elif m == 2:
        result = [3, 5, 6, 9, 10, 12, 17, 18, 20, 24, 33, 34, 36, 40, 48]
    elif m == 3:
        result = [7, 11, 13, 14, 19, 21, 22, 25, 26,
                  28, 35, 37, 38, 41, 42, 44, 49, 50, 52, 56]
    elif m == 4:
        result = [15, 23, 27, 29, 30, 39, 43, 45, 46, 51, 53, 54, 57, 58, 60]
    elif m == 5:
        result = [31, 47, 55, 59]
    return result


def bw(n):
    if n == 1:
        for i in hour(1):
            print('%s:00' % i)
    elif n == 2:
        for i in hour(2):
            print('%s:00' % i)
        for i in hour(1):
            for j in minute(1):
                print('%s:%s' % (i, j))
    elif n == 3:
        for i in hour(3):
            print('%s:00' % i)
        for i in hour(2):
            for j in minute(1):
                print('%s:%s' % (i, j))
        for i in hour(1):
            for j in minute(2):
                print('%s:%s' % (i, j))
    elif n == 4:
        for i in hour(3):
            for j in minute(1):
                print('%s:%s' % (i, j))
        for i in hour(2):
            for j in minute(2):
                print('%s:%s' % (i, j))
        for i in hour(1):
            for j in minute(3):
                print('%s:%s' % (i, j))
    elif n == 5:
        for i in hour(3):
            for j in minute(2):
                print('%s:%s' % (i, j))
        for i in hour(2):
            for j in minute(3):
                print('%s:%s' % (i, j))
        for i in hour(1):
            for j in minute(4):
                print('%s:%s' % (i, j))
    elif n == 6:
        for i in hour(3):
            for j in minute(3):
                print('%s:%s' % (i, j))
        for i in hour(2):
            for j in minute(4):
                print('%s:%s' % (i, j))
        for i in hour(1):
            for j in minute(5):
                print('%s:%s' % (i, j))
    elif n == 7:
        for i in hour(3):
            for j in minute(4):
                print('%s:%s' % (i, j))
        for i in hour(2):
            for j in minute(5):
                print('%s:%s' % (i, j))
    elif n == 8:
        for i in hour(3):
            for j in minute(5):
                print('%s:%s' % (i, j))


bw(4)
