#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-22 09:14:19
from nodefun import Tree


t = Tree()
a = [1, 2, 3, 4, 5]
for i in a:
    t.add(i)
c = t.traverse_by_layer(t.root.left)
d = t.traverse_by_layer(t.root.right)
e = max(x.layer for x in c) + max(y.layer for y in d)
print(e)
