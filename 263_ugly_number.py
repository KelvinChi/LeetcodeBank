#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def ugly_number(num):
    a = divide(num, 2)
    b = divide(a, 5)
    c = divide(b, 3)
    print('Yes, it is an ugly number') if c == 1 else print('Not, it is not an ugly number')


def divide(num, divide_num):
    a = num
    #  print(a)
    while a % divide_num == 0:
        a /= divide_num
    else:
        return a


if __name__ == '__main__':
    ugly_number(8)
    ugly_number(6)
    ugly_number(14)
