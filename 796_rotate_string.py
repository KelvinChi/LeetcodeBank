#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def rs(A, B):
    length = len(B)
    for i in range(1, length):
        if B[:i] in A and B[i:] in A:
            return True
    return False


A = 'abcde'
B = 'cdeab'
print(rs(A, B))

C = 'abcde'
D = 'abced'
print(rs(C, D))
