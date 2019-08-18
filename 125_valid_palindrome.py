#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def valid_palindrome(string):
    temp = str_judge(string)
    num = len(temp) // 2
    if temp[:num] == ''.join(list(reversed(temp[-num:]))):
        print('Yes, it is.')
    else:
        print("No, it isn't.")


def str_judge(string):
    temp = []
    for i in string:
        if i.isalnum():
            temp.append(i)
    result = ''.join(temp)
    return result.lower()


a = r'A man, a plan, a canal: Panama'
print(str_judge(a))
valid_palindrome(a)

b = 'race a car'
valid_palindrome(b)