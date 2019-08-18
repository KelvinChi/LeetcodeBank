#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-20 07:59:30


def rr(lis):
    dic = dict.fromkeys(lis, '0')
    print(dic)
    lis.sort(reverse=True)
    print(lis)
    count = 4
    for key in dic.keys():
        #  for i in range(len(lis)):
        if key == lis[0]:
            dic[key] = 'Gold Medel'
        elif key == lis[1]:
            dic[key] = 'Silver Medal'
        elif key == lis[2]:
            dic[key] = 'Bronze Medal'
        else:
            dic[key] = str(count)
            count += 1
    print(dic)


lis = [6, 5, 9, 8, 4, 1, 7]
rr(lis)
