#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def feedback_num(word):
    num = [0] * len(word)
    for i in range(1, len(word)):
        if word[i] != word[i - 1]:
            num[i] = num[i - 1] + 1
        else:
            num[i] = num[i - 1]
    return num


first_word = input('pls input the first word')
second_word = input('pls input the second word')
if feedback_num(first_word) == feedback_num(second_word):
    print('yes')
else:
    print('no')

