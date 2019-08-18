#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-29 07:40:44


def misotl(lis1, lis2):
    temp = list(set(lis1).intersection(set(lis2)))
    count = []
    for i in temp:
        count.append((lis1.index(i), lis2.index(i)))
    sumIndex = [sum(x) for x in count]
    minSumIndex = min(sumIndex)
    for x in count:
        if sum(x) == minSumIndex:
            print(lis1[x[0]])


lis1 = ["Shogun", "KFC", "Tapioca Express", "Burger King"]
lis2 = ["KFC", "Shogun", "Burger King"]
misotl(lis1, lis2)
