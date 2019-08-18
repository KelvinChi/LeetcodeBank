#!/usr/bin/env python3
# encoding: utf-8


def judge(string):
    lis = list(string)
    count = 0
    for i in range(len(lis) // 2):
        if lis[i] == lis[-1 - i]:
            count += 1
        else:
            return False
    if count == len(lis) // 2:
        return True


def get_index_list(lis):
    result = []
    for i in lis:
        if lis.count(i) % 2 == 1:
            result.append(lis.index(i))
            break
    else:
        return
    for j in range(1, lis.count(i)):
        result.append(lis[result[-1] + 1:].index(i) + result[-1] + 1)
    return result


def vpii(string):
    temp = list(string)
    temp1 = list(temp)
    for i in range(len(string)):
        temp.pop(i)
        if judge(temp):
            print('True')
            return
        else:
            temp = temp1
            if i == len(string) - 1:
                print('False')



lis = '13234321'
print(get_index_list(lis))
print(str(judge('1234321')))
vpii(lis)
