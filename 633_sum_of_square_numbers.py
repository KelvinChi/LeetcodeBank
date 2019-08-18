#!/usr/bin/env python3
# encoding: utf-8


def sosn(num):
    if num == 0:
        print('True')
        return
    for i in range(0, int(num ** 0.5)):
        if ((num - (i ** 2)) ** 0.5) % 1 == 0:
            print('True')
            return
        elif i == int(num ** 0.5) - 1:
            print('False')


for j in range(100):
    print(j)
    sosn(j)
