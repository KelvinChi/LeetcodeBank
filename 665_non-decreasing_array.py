#!/usr/bin/env python3
# encoding: utf-8


def judge(lis):
    for i in range(len(lis)):
        try:
            if lis[i] > lis[i + 1]:
                return False
        except IndexError:
            return True


def nda(lis):
    for i in range(len(lis) - 1):
        if lis[i] > lis[i + 1]:
            lis[i] = lis[i + 1]
            break
    return judge(lis)


lis = [1, 4, 2, 3]
print(str(nda(lis)))
