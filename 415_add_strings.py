#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-11 05:54:19


def get_int(string):
    a = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
         '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    for key, value in a.items():
        if string == key:
            return value


def change(num):
    a = list(num)
    b = []
    c = 0
    for i in a:
        i = get_int(i)
        b.append(i)
    b.reverse()
    for j in range(len(b)):
        c += b[j] * (10 ** j)
    return c


def as_fun(num1, num2):
    result = change(num1) + change(num2)
    return result


num1 = '2143254123564'
num2 = '98767868923'
print(as_fun(num1, num2))
