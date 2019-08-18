#!/usr/bin/env python
# -*- coding:utf8 -*-
# Created by CK 2019-04-28 05:09:30


def rvoas(word):
    lis = list(word)
    vowels = ['a', 'e', 'i', 'o', 'u']
    position = [0]
    vowels_lis = []
    consonant_lis = []
    for i in range(len(lis)):
        if lis[i] in vowels:
            position.append(lis.index(lis[i], i))
            vowels_lis.insert(0, lis[i])
        else:
            consonant_lis.append(lis[i])
    for i in range(len(position[1:])):
        consonant_lis.insert(position[i + 1], vowels_lis[i])
    result = ''.join(consonant_lis)
    return result


word = 'whet is the fuck'
print(rvoas(word))
