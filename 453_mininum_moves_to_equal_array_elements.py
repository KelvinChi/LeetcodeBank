#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-17 08:11:33


def mmteae(lis):
    return sum(lis) - len(lis)*min(lis)


lis = [3, 7, 11, 24]
print(mmteae(lis))
