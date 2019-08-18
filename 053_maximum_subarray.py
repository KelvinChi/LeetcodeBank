#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


a = [-2,1,-3,4,-1,2,1,-5,4]


def ms(l):
    sum, reg = 0, l[0]
    for i in l:
        sum = max(sum + i, i)
        reg = max(reg, sum)
    return reg


b = ms(a)
print(b)
