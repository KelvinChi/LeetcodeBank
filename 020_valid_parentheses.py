#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def pair(a, b):
    if a == '(' and b == ')':
        return True
    elif a == '[' and b == ']':
        return True
    elif a == '{' and b == '}':
        return True
    else:
        return False


def la(string):
    if string == '':
        return 'True'
    else:
        a = list(string)
        for i in range(1, len(a)):
            if pair(a[i - 1], a[i]):
                a[i - 1] = ' '
                a[i] = ' '
        c = ''.join(a)
        b = c.replace(' ', '')
        if string != b:
            return b
        else:
            return 'False'


def judge(string):
    st = la(string)
    while True:
        if st == 'False' or st == 'True':
            print(st)
            break
        else:
            st = la(st)
            continue


if __name__ == '__main__':
    s1 = '[]{()}'
    s2 = '[]{(})'
    s3 = '[]'
    judge(s1)
    judge(s2)
    judge(s3)
