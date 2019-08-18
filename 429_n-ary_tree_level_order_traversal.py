#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-14 08:16:54
# This document is just for Traversal method,
# let us assume this is a 3-ary tree.


def ntlot(root):
    if root is None:
        return
    lis1 = [root]
    lis2 = []
    while lis1 is not None:
        for i in lis1:
            if i.b1 is not None:
                lis2.append(i.b1)
                print(i.b1)
            elif i.b2 is not None:
                lis2.append(i.b2)
                print(i.b2)
            elif i.b1 is not None:
                lis2.append(i.b3)
                print(i.b3)
        lis1 = lis2
        lis2 = []
