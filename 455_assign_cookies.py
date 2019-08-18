#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-17 08:22:11


def ac(lis1, lis2):
    lis1.sort()
    lis2.sort()
    count = 0
    for i in lis1:
        for j in lis2:
            if i > j:
                lis2.pop(0)
            else:
                count += 1
                lis2.pop(0)
                break
    return count


lis1 = [1, 2]
lis2 = [2, 3, 4]
print(ac(lis1, lis2))
