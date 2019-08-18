#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def cas(n):
    # 不考虑n小于0的情况
    if n == 1:
        return '1'
    elif n == 2:
        return '11'
    else:
        a = '11'
        count = 2
        b = 1
        while count < n:
            e = []
            d = list(a)
            for i in range(1, len(d)):
                if d[i] == d[i - 1]:
                    b += 1
                    a = str(b) + d[i - 1]
                    if i == len(d) - 1:
                        e.append(a)
                        b = 1
                        break
                elif d[i] != d[i - 1]:
                    a = str(b) + d[i - 1]
                    b = 1
                    e.append(a)
                    if i == len(d) - 1:
                        f = str(1) + d[i]
                        e.append(f)
                        b = 1
                        break
            count += 1
            a = ''.join(e)
        return a


for i in range(1, 20):
    a = cas(i)
    print(a)

