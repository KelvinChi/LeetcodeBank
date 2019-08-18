#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def power_of_two(num):
    a = []
    r = 30
    for i in range(r):
        a.append(2**i)
    if num in a:
        print('True')
    elif r_2(num, r) in a:
        print('True')
    elif r_2(r_2(num, r), r) in a:
        print('True')
    else:
        two(r_2(r_2(num, r), r))


def r_2(num, r):
    a = num / (2 ** (r / 2))
    return a


def two(num):
    a = num
    while a > 1:
        a /= 2
    print('True') if a == 1 else print('False')


get_num = int(input('pls input what you want'))
power_of_two(get_num)

