#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


a = [1, 3, 4, 6, 8, 9, 4, 5, 6, 4, 8]
for i in range(a.count(4)):
    a.remove(4)
print(a)
