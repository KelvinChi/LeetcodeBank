#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def majority_element(lis):
    a = set(lis)
    c = 0
    d = 0
    for i in a:
        b = lis.count(i)
        if b > c:
            c = b
            d = i
    return d if c > len(lis) / 2 else None


lis = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(lis))