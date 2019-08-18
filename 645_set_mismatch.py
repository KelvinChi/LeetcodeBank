#!/usr/bin/env python3
# encoding: utf-8


def sm(lis):
    for i in range(1, len(lis)):
        if lis[i] == lis[i - 1]:
            lis[i] = i + 1
            return i, i + 1


lis = [2, 2]
print(sm(lis))