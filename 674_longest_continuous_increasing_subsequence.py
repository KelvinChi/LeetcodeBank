#!/usr/bin/env python3
# encoding: utf-8


def lcis(lis):
    result = [lis[0]]
    for i in range(len(lis) - 1):
        if lis[i] < lis[i + 1]:
            result.append(lis[i + 1])
        else:
            return len(result)
    return len(result)


lis = [1, 3, 5, 4, 7]
print(lcis(lis))
