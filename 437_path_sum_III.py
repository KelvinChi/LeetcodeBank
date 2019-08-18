#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-16 03:03:53
from nodefun import Tree


if __name__ == '__main__':
    count = 0
    sum = 8
    t = Tree()
    result = []
    a = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    for i in a:
        t.add(i)
    b = t.traverse_by_layer(t.root)
    for j in b:
        t.num_to_list(j)
        # print(t.n_t_l)
        if sum in t.n_t_l:
            count += 1
        t.n_t_l = []
    print(count)
