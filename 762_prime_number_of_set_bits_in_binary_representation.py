#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def count_one(string):
    num = 0
    for i in string:
        if i == '1':
            num += 1
    return num


def judge(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def pnosbibr(L, R):
    result = 0
    for i in range(L, R + 1):
        a = bin(i)
        num = count_one(a[2:])
        if judge(num):
            result += 1
    return result


L = 10
R = 158
print(pnosbibr(L, R))
