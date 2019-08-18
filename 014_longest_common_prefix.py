#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def small_output(item_1, item_2):
    return len(item_1) if len(item_1) < len(item_2) else len(item_2)


def original_list(ll):
    length = len(ll)
    nl = []
    for i in range(length // 2):
        nl_i = []
        a = ll[i]
        b = ll[(length // 2) + (length % 2) + i]
        for j in range(small_output(a, b)):
            if a[j] == b[j]:
                nl_i.append(a[j])
            else:
                break
        nl.append(''.join(nl_i))
    if length % 2 == 1:
        nl.append(ll[length // 2])
    return nl


def result(nl):
    nl = original_list(nl)
    result(nl) if len(nl) != 1 else print(nl)


a = ['leet', 'leen', 'leit', 'leha', 'lh']
print(len(a))
print(original_list(a))
result(a)
