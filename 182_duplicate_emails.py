#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


# 简化了程度，核心概念没问题，算法效率暂不考虑

a = {1: 'a@b.com', 2: 'c@d.com', 3: 'a@b.com', 4: 'a@b.com'}
keys = []
values = []
list = []
for i, j in a.items():
    if j not in values:
        values.append(j)
    else:
        print('%s重复了，对应键为%s' % (j, i))
