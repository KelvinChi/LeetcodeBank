#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def missing_number(lis):
    a = min(lis)
    b = max(lis)
    pin = 0
    for i in range(a + 1, b):
        if i not in lis:
            print(i)
            pin += 1
    print('nothing left') if pin == 0 else print('%d number(s) left' % pin)


if __name__ == '__main__':
    lis = [1, 2, 8, 7, 5, 6, 1, 12, 5, 8, 6]
    missing_number(lis)
