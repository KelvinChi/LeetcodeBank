#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def judge_prime(num):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        return num


d = 0
for i in range(1000):
    if judge_prime(i):
        d += 1
print(d)

