#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-30 08:45:30


def cpf(flowerbed, n):
    count = []
    result = []
    final = 0
    if flowerbed[1] == 0:
        count.append(0)
    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i - 1] == 1 and flowerbed[i] == 0:
            count.append(i)
        elif flowerbed[i] == 1 and flowerbed[i - 1] == 0:
            count.append(i - 1)
    if flowerbed[-1] == 0:
        count.append(len(flowerbed) - 1)
        final += 1
    print(count)
    for x in range(0, len(count), 2):
        result.append(count[x + 1] - count[x])
    print(result)
    for z in result:
        final += z // 2
    if count[0] == 0 and result[0] % 2 == 1:
        final += 1
    if count[-1] == 0 and result[-1] % 2 == 1:
        final += 1
    if final >= n:
        return True
    else:
        return False


flowerbed = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
n = 4
print(str(cpf(flowerbed, n)))
flowerbed = [1, 0, 0, 0, 1]
n = 1
print(str(cpf(flowerbed, n)))
flowerbed = [1, 0, 0, 0, 1]
n = 2
print(str(cpf(flowerbed, n)))
