#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


a = 'Let us get up!'
b = a.split(' ')
d = []
for i in b:
    c = []
    for j in i:
        if j.isalpha():
            c.append(j)
    d.append(''.join(c))
print(d)
print(len(d[len(d) - 1]))
