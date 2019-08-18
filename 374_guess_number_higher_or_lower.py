#!/usr/bin/env python
# -*- coding:utf8 -*-
# Created by CK 2019-04-29 08:26:06
import random


def guess():
    num = random.randint(1, 1000)
    step = 0
    while True:
        temp = int(input('input a number'))
        if temp < num:
            print('your num is smaller')
            step += 1
            continue
        elif temp > num:
            print('your num is bigger')
            step += 1
            continue
        else:
            step += 1
            print('BINGO!!!You have guessed %s times!!!' % step)
            break


guess()
