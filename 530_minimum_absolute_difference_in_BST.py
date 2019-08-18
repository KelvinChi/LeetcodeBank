#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-22 02:58:13
from nodefun import Tree


t = Tree()
minus = []
a = [6, 2, 1, 5, 7, 9, 0, 3, 4, None, 8]
for i in a:
    t.add(i)
for i in t.traverse_by_layer(t.root):
    if str(i) == 'None' or str(i.father) == 'None':
        pass
    else:
        minus.append(abs(int(str(i.father)) - int(str(i))))
print(minus)
print(min(minus))
