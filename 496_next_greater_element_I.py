#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-20 03:26:00


def ngei(num1, num2):
    result = []
    for i in num1:
        result.append(judge(i, num2))
    return result


def judge(i, num2):
    temp = num2.index(i)
    if temp == len(num2):
        return -1
    else:
        for j in range(temp, len(num2)):
            if num2[j] > i:
                return num2[j]
        else:
            return -1


num1 = [4, 1, 2]
num2 = [1, 3, 4, 2]
print(ngei(num1, num2))
