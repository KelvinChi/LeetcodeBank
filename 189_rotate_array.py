#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


a = list(range(8))
print('a is %s' % str(a))
b = a.copy()
move_step = int(input('pls input a int number'))
equal_step = move_step % len(a)


def pin(num, length):
    return num if num < length else num - length


# first
for i in range(len(a)):
    b[pin(i + equal_step, len(a))] = a[i]
print('b is %s' % str(b))

# second
c = a[-equal_step:] + a[:len(a) - equal_step]
print('c is %s' % str(c))

# third
d = []
for i in range(len(a) - equal_step, len(a)):
    d.append(a[i])
for i in range(0, len(a) - equal_step):
    d.append(a[i])
print('d is %s' % str(d))
