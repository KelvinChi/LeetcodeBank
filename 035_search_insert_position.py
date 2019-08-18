#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def sip(l, v):
    try:
        a = l.index(v)
        return a
    except ValueError:
        l.append(v)
        b = l.index(v)
        return b


a = [1, 3, 5, 6]
b = 5
c = sip(a, b)
print(c)


d = [1, 3, 5, 6]
e = 7
f = sip(d, e)
print(f)