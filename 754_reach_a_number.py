#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def ram(target):
    pin = 1
    s = 1
    while s < target:
        pin += 1
        s = (pin ** 2 + pin) / 2
    if s == target:
        return pin
    s = (pin ** 2 - pin) / 2
    pin -= 1
    return int(pin + (target - s) * 2)


target = 221
print(ram(target))
