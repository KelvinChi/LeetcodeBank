#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


import random

b = []
c = 0
d = 0
for i in range(20):
    a = random.randint(1, 20)
    b.append(a)

for i in range(1, len(b), 2):
    c += b[i]

for i in range(2, len(b), 2):
    d += b[i]

print(b)
print(c)
print(d)

