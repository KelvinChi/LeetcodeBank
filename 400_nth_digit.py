#!/usr/bin/env python
# -*- coding:utf8 -*-
# Created by CK 2019-04-30 05:14:51


def nd(n):
    amount = 0
    for i in range(9):
        pin = amount
        amount = int(str(i)+(str(8)*i)+'9')
        if n < amount:
            sub = n - pin
            count_num = (sub // (i + 1)) + (10 ** i)
            lis = str(count_num - 1)[-1] + str(count_num)[:i + 1]
            return lis[sub % (i + 1)]


while True:
    n = input('input a number you want \n')
    try:
        temp = int(n)
        print('The result is %s.' % nd(temp))
    except ValueError:
        if n == 'q':
            exit()
        else:
            print('your input is unlawful, pls input a number or q')
            continue
