#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


import re
a = ['987-123-4567', '123 456 7890', '(123) 456-7890']
for i in a:
    b = re.findall(r'\d{3}-\d{3}-\d{4}', i)
    c = re.findall(r'\(\d{3}\)\ \d{3}-\d{4}', i)
    if b:
        print(b)
    if c:
        print(c)
