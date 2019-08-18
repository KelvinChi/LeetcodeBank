#!/usr/bin/env python
# -*- coding:utf8 -*-
# Created by CK 2019-04-12 01:50:41


def move_zeroes(lis):
    znum = lis.count(0)
    for i in range(znum):
        lis.remove(0)
    lis.extend([0]*znum)
    print(lis)


if __name__ == "__main__":
    lis = [0, 1, 2, 0, 4, 0, 6, 8, 0]
    move_zeroes(lis)
