#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def add_nums(num):
    a = list(str(num))
    b = 0
    for i in a:
        b += int(i)
    return b


def add_digits(num):
    a = 10
    b = num
    while a not in range(10):
        a = add_nums(b)
        b = a
    else:
        print(a)


#  num = int(input('input a number you want'))
num = 1369818841786818651981684198641
add_digits(num)
#  print(add_nums(38))
