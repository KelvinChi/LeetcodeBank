#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-29 01:51:25
from nodefun import Tree


def add_to_list(tree):
    result = []
    for i in Tree().traverse_by_layer(tree):
        result.append(i.value)
    return result


def compare(a, b):
    if str(a) == str(b):
        if add_to_list(a) == add_to_list(b):
            return True
    try:
        compare(a.left, b)
        compare(a.right, b)
    except AttributeError:
        pass


t = Tree()
for i in [3, 4, 5, 1, 2]:
    t.add(i)
t1 = Tree()
for x in [4, 1, 2, 0]:
    t1.add(x)
a = t.root
b = t1.root
if compare(a, b):
    print('True')
else:
    print('False')
