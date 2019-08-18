#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-29 06:37:51
import numpy as np


def raii(m, n, operations):
    array = np.zeros((m, n))
    r = len(operations)
    for i in range(r):
        for x in range(operations[i][0]):
            for y in range(operations[i][1]):
                array[x][y] += 1
    print(array)


m = 3
n = 3
operations = [[2, 2], [3, 3]]
raii(m, n, operations)
