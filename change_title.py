#!/usr/bin/env python3
# encoding: utf-8
import re
import pyperclip


def change_title(string):
    temp = re.findall(r'(\w*?)\.*?\s(.*)', string)
    result = [temp[0][0]]
    for i in temp[0][1].split(' '):
        if i.upper() == i:
            result.append(i)
        else:
            result.append(i.lower())
    result = '_'.join(result)
    return result + '.py'


s = input('Input q for quit \nPls input the title\n')
result = change_title(s)
pyperclip.copy(result)
print('Name had copied to shear plate~')
