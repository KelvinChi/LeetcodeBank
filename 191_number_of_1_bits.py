#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


while True:
    try:
        d = int(input('pls input a int number'))
        break
    except ValueError:
        print('input wrong, pls try again')


a = bin(d)[2:]
print(a)
b = a.count('1')
print(b)
