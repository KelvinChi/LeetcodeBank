#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def rdfsa(l):
    a = list(set(l))
    for i in range(len(a)):
        l[i] = a[i]
    return len(a), l


nums = [0,0,1,1,1,2,2,3,3,4]
result = rdfsa(nums)
print(result)
