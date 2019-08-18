#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def reverse_num():
    a = input('请输入整数')
    while True:
        try:
            int(a)
            break
        except ValueError:
            a = input('输入有误请重新输入')
            continue
    ls = list(str(a))
    if ls[0] == '-' and int(a) in range(-2**31, 2**31 - 1):
        temp_1 = ls[1: len(ls)]
        temp_1.insert(len(ls), '-')
        temp_2 = list(reversed(temp_1))
        return ''.join(temp_2)
    elif ls[0] == '0' and int(a) in range(-2**31, 2**31 - 1):
        result_ls = list(reversed(ls[1: len(ls)]))
        return ''.join(result_ls)
    else:
        return 0


if __name__ == '__main__':
    te = reverse_num()
    print(te)
