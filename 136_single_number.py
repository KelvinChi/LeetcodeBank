#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


# 线性复杂度不是很懂，先这样吧
a = [4,1,2,1,2]

for i in a:
    b = a.count(i)
    if b == 1:
        print(b)
