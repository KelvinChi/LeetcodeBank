#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def fac(x):
    # 计算阶乘
    y = 1
    if x == 0:
        y = 1
    else:
        for i in range(1, x + 1):
            y *= i
    return y


def c(m, n):
    # 计算C
    return fac(m) / (fac(m - n) * fac(n)) if m > n else fac(n) / (fac(n - m) * fac(m))


def count(x):
    # 计算全部数量
    count = 0
    for i in range(0, x // 2 + 1):
        n = i
        m = x - 2 * i
        if m > n:
            count += c(m + 1, n)
            print('此时有%d个1，%d个2，单方案种类有%d种，总数为%d种' % (m, n, c(m + 1, n), count))
        else:
            count += c(n + 1, m)
            print('此时有%d个1，%d个2，单方案种类有%d种，总数为%d种' % (m, n, c(m + 1, n), count))
    return count


print(fac(10))
print(c(5, 10))
step = 4
print('当总台阶有%d时，总方案数有%d种'% (step, count(step)))
