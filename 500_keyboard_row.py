#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-20 03:36:25


def kr(lis):
    a = sorted(list('qwertyuiop'))
    b = sorted(list('asdfgjkl'))
    c = sorted(list('zxcvbnm'))
    result = []
    for i in lis:
        count1 = 0
        count2 = 0
        count3 = 0
        temp = ''.join(sorted(list(set(list(i.lower())))))
        for j in temp:
            if j in a:
                count1 += 1
            elif j in b:
                count2 += 1
            elif j in c:
                count3 += 1
        if count1 == len(temp) or count2 == len(temp) or count3 == len(temp):
            result.append(i)
    return result


lis = ["Hello", "Alaska", "Dad", "Peace"]
print(kr(lis))
