#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-20 07:08:00


from nodefun import Tree


a = [1, None, 2, 2]
t = Tree()
for i in a:
    t.add(i)
lis = [str(t.root)]
for j in t.traverse_by_layer(t.root):
    lis.append(str(j))
temp = list(set(lis))
dic = {}
result = []
for x in temp:
    dic[x] = lis.count(x)
for key, value in dic.items():
    if value == max(list(dic.values())):
        result.append(key)
print(result)
