#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-14 08:38:34
import re


def nosias(string):
    a = re.findall(r'[ ]*([a-zA-Z\']+)[ ]*', string)
    print(len(a))


b = 'unlimited times, as many times as possible, giving back as needed lr'
nosias(b)
