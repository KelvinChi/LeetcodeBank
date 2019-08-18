#!/usr/bin/env python3
# encoding: utf-8


def bg(lis):
    temp = []
    for i in lis:
        try:
            temp.append(int(i))
        except ValueError:
            if i == 'C':
                temp.pop()
            elif i == 'D':
                temp.append(temp[-1] * 2)
            elif i == '+':
                temp.append(temp[-1] + temp[-2])
    return sum(temp)


lis = ["5","-2","4","C","D","9","+","+"]
print(bg(lis))