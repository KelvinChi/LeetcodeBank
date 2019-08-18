#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-19 13:46:34


def ip(lis):
    count = 0
    for i in range(len(lis)):
        for j in range(len(lis[0])):
            if a[i][j] == 1:
                try:
                    if a[i - 1][j] == 0 or i == 0:
                        count += 1
                except IndexError:
                    count += 1
                try:
                    if a[i + 1][j] == 0:
                        count += 1
                except IndexError:
                    count += 1
                try:
                    if a[i][j - 1] == 0 or j == 0:
                        count += 1
                except IndexError:
                    count += 1
                try:
                    if a[i][j + 1] == 0:
                        count += 1
                except IndexError:
                    count += 1
    return count


a = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(ip(a))
