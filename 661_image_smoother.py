#!/usr/bin/env python3
# encoding: utf-8
import numpy as np


def ims(array):
    result = np.zeros((len(array), len(array[0])))
    temp = []
    for i in range(len(array)):
        for j in range(len(array[0])):
            temp.append(array[i][j])
            try:
                temp.append(array[i][j + 1])
            except IndexError:
                pass
            try:
                temp.append(array[i + 1][j + 1])
            except IndexError:
                pass
            try:
                temp.append(array[i + 1][j])
            except IndexError:
                pass
            try:
                if j != 0:
                    temp.append(array[i + 1][j - 1])
            except IndexError:
                pass
            try:
                if j != 0:
                    temp.append(array[i][j - 1])
            except IndexError:
                pass
            try:
                if i != 0 and j != 0:
                    temp.append(array[i - 1][j - 1])
            except IndexError:
                pass
            try:
                if i != 0:
                    temp.append(array[i - 1][j])
            except IndexError:
                pass
            try:
                if i != 0:
                    temp.append(array[i - 1][j + 1])
            except IndexError:
                pass
            result[i][j] = sum(temp) // len(temp)
            temp = []
    return result


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
print(ims(array))
