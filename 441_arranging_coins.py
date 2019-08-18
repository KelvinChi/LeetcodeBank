#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-17 02:58:57


def ac(num):
    for i in range(2 ** 16):
        a = (i ** 2 + i) / 2
        if a > num:
            print(i - 1)
            break


n = 52334351581684
ac(n)
