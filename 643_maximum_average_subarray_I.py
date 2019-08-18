#!/usr/bin/env python3
# encoding: utf-8


def masi(lis, k):
    sumfour = 0
    for i in range(len(lis) - k + 1):
        temp = lis[i: i + k]
        sumfour = sum(temp) if sumfour < sum(temp) else sumfour
        result = sumfour / k
    return result


lis = [1, 12, -5, -6, 50, 3]
k = 4
print(masi(lis, k))
