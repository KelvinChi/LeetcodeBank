#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-22 06:00:05
from nodefun import Tree


t = Tree()
a = [6, 2, 1, 5, 7, 9, 0, 3, 4, None, 8]
for i in a:
    t.add(i)
b = t.traverse_by_layer(t.root)
temp = []
for j in b:
    if str(j) == 'None':
        temp.append(None)
    else:
        temp.append(int(str(j)))
final = []
get = temp.copy()
for y in get:
    if y == None:
        get.remove(None)
get.sort(reverse=True)
for x in temp:
    if x == None:
        final.append(None)
    else:
        final.append(sum(get[:get.index(x) + 1]))
result = Tree()
for z in final:
    result.add(z)
haha = result.traverse_by_layer(result.root)
for abc in haha:
    print(abc, end=' ')
