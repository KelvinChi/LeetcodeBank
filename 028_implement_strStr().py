#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def implement_str(a, b):
    try:
        result = a.index(b)
        return result
    except ValueError:
        return -1


haystack = 'hello'
needle = 'll'
a = implement_str(haystack, needle)
print(a)

haystack = "aaaaa"
needle = "bba"
b = implement_str(haystack, needle)
print(b)
