#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def palindrome_linked_list(string):
    lis = list(string)
    count = 0
    for i in range(len(lis) // 2):
        if lis[i] == lis[-1 - i]:
            count += 1
        else:
            print("False")
            break
    if count == len(lis) // 2:
        print('True')


num = input('input a number you want')
palindrome_linked_list(num)

