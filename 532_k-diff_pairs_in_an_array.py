#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-22 03:28:54


def kdpiaa(lis, k):
    result = 0
    flag = []
    if k == 0:
        for i in lis:
            if i not in flag:
                flag.append(i)
                if lis.count(i) >= 2:
                    result += 1
        return result
    elif k < 0:
        return 0
    else:
        temp = list(set(lis))
        temp.sort()
        for i in temp:
            if i + k in temp:
                result += 1
        return result


lis = [3, 1, 4, 1, 5]
k = 0
print(kdpiaa(lis, k))
ha = [1, 2, 3, 4, 5]
k1 = -1
print(kdpiaa(ha, k1))
