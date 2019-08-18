#!/usr/bin/env python3
# encoding: utf-8


def rsm(A, B):
    for i in range(1, 10000 // len(A)):
        if B in A * i:
            return i


A = 'abcd'
B = 'cdabcdab'
print(rsm(A, B))