#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-31 03:19:25
from nodefun import Tree


# 因为可实现层序遍历，所以直接列表操作就好
a = [1, 3, 2, 5]
b = [2, 1, 3, None, 4, None, 7]
for i in range(len(b) - len(a)):
    a.append(None)
newlis = []
for j in range(len(b)):
    if a[j] == b[j] is None:
        newlis.append(None)
    elif a[j] is None:
        newlis.append(b[j])
    elif b[j] is None:
        newlis.append(a[j])
    else:
        newlis.append(a[j] + b[j])
t = Tree()
for x in newlis:
    t.add(x)
t.tree_structure(t.root)
