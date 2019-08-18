#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-31 02:59:53
from nodefun import Tree


def csfbt(tree):
    if tree is None:
        return
    if tree.father is None:
        print(tree, end='')
    else:
        print('(' + str(tree.value), end='')
    csfbt(tree.left)
    csfbt(tree.right)
    if tree.father is None:
        pass
    else:
        print(')', end='')


tree = Tree()
for i in [1, 2, 3, 4]:
    tree.add(i)
csfbt(tree.root)
