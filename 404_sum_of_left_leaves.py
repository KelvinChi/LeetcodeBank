#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-09 04:57:05


from nodefun import Tree

result = []
lis = [3, 9, 20, 15, 7]
tree = Tree()
for i in lis:
    tree.add(i)
tree.get_left_leaves(tree.root)
for j in tree.lis:
    result.append(int(str(j)))
print(sum(result))
