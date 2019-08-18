#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def umcw(lis):
    result = []
    for i in lis:
        temp = i.upper()
        morse = ''
        for j in temp:
            morse += transfer(j)
        result.append(morse)
    return len(set(result))

def transfer(alpha):
    global dict
    for key, value in dict.items():
        if alpha == key:
            return value


dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}


lis = ['gin', 'zen', 'gig', 'msg']
print(umcw(lis))
