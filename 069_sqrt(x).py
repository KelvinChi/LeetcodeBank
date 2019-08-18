#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


# 算法很差，甚至不如二分法的效率，但现阶段能做出来就ok了
def sqrt_bin(num):
    count = 2
    x = num / count
    while count < 20:
        if x ** 2 > num:
            count += 1
            x = x - num / count
        else:
            count += 1
            x = x + num / count
        print(count, x)
    return x


a = sqrt_bin(8)
print(a)



