#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def palindrome_number(num):
    if num < 0:
        print('非回文数')
    else:
        count = []
        l = len(str(num))
        for i in range(1, l // 2 + 1):
            if (num % (10 ** i)) // (10 ** (i - 1)) == (num // (10 ** (l - i))) % 10:
                count.append(1)
            else:
                print('非回文数')
                break
        if sum(count) == l // 2:
            print('是回文数')


if __name__ == '__main__':
    a = int(input('请输入一个整数'))
    palindrome_number(a)
