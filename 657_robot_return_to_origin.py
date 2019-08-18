#!/usr/bin/env python3
# encoding: utf-8


def rrto(string):
    temp = list(string)
    # if temp.count('U') == temp.count('D') and temp.count('R') == temp.count('L'):
    #     return True
    # else:
    #     return False
    return True if temp.count('U') == temp.count('D') and \
                   temp.count('R') == temp.count('L') else False


string = 'UD'
print(str(rrto(string)))