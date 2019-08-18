#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def factorial_trailing_zeroes(num):
    mul = 1
    a = range(2, num + 1, 2)
    b = range(5, num + 1, 10)
    for i in a:
        mul *= i
    for j in b:
        mul *= j
    count = 0
    temp = str(mul)
    while temp[-1] == '0':
        count += 1
        temp = temp[:-1]
    return count


print(factorial_trailing_zeroes(10))

