#!/usr/bin/env python
# -*- coding:utf8 -*-
# Created by CK 2019-04-28 03:28:13


def sumRange(start, end):
    nums = [-2, 0, 3, -5, 2, -1]
    temp = nums[start:end + 1]
    return sum(temp)


print(sumRange(0, 2))
print(sumRange(2, 5))
print(sumRange(0, 5))
