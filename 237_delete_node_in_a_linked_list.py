#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def node(lis, num):
    a = lis.index(num)
    del(lis[a])
    return lis


lis = [4, 1, 5, 9]
print(lis)
num = int(input('input a number'))
print(node(lis, num))

