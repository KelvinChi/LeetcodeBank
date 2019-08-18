#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def index_lis(ele, lis, num):
    b = [-1]
    c = 0
    for i in range(num):
        d = lis[b[-1] + 1:].index(ele) + c
        b.append(d)
        c = b[-1] + 1
    return b[1:]


def get_all_min_num(lis):
    s = set(lis)
    all = []
    for i in s:
        pin = len(lis)
        c = lis.count(i)
        index_num = index_lis(i, lis, c)
        # print(i, c, index_num)
        if c > 1:
            for j in range(1, len(index_num)):
                if index_num[j] - index_num[j - 1] < pin:
                    pin = index_num[j] - index_num[j - 1]
            all.append(pin)
    return min(all)


a = [1, 2, 4, 6, 1, 3, 5, 1, 6, 7, 1]
k = 5
result_list = get_all_min_num(a)
if result_list <= 3:
    print('True')
else:
    print('False')
