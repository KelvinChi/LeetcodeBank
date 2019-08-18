#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def best_time(num):
    for k in range(len(num)):
        if num[k] == min(num):
            if k == len(num) - 1:
                print('收入为0')
            else:
                print('收入为' + str(max(num[k:]) - num[k]))


a = [0, 1, 5, 3, 2, 4, 3, 6, 9, 3, 5, 8, 6, 9, 1, 5, 10]
b = [6, 5, 4, 2, 1]
best_time(a)
best_time(b)


def best_time_2(num_1):
    data = []
    for k in range(len(num_1)):
        if k == 0:
            if a[k] < a[k + 1]:
                print('buy at 0')
                value = a[k]
            else:
                pass
        elif k < len(num_1) - 1:
            if a[k] < a[k - 1] and a[k] < a[k + 1]:
                print('buy at ' + str(k))
                value = a[k]
            elif a[k] > a[k - 1] and a[k] > a[k + 1]:
                print('sell at' + str(k))
                result = a[k] - value
                data.append(result)
        elif k == len(num_1) - 1 and a[k] > a[k - 1]:
            print('sell at' + str(k))
            result = a[k] - value
            data.append(result)
    return sum(data)
    # return data


c = best_time_2(a)
print('收入为' + str(c))
