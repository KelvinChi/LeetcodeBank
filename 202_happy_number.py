#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def get_num_list(num):
    result = []
    while len(str(num)) > 1:
        result.append(num % 10)
        num //= 10
    result.append(num % 10)
    result = result[::-1]
    return result


def happy_number(num, pin):
    temp = get_num_list(num)
    new_num = 0
    for i in temp:
        new_num += i ** 2
    if new_num == 4 or new_num == 0:
        # print(str(pin) + ' is no happy')
        pass
    elif new_num == 1:
        print(str(pin) + ' is happy')
    else:
        happy_number(new_num, pin)


for i in range(100):
    happy_number(i, i)
