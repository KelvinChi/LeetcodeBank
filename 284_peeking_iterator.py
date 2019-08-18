#!/usr/bin/env python
# -*- coding:utf8 -*-
# Created by CK 2019-04-16 06:24:48


class Peeking_iterator:
    def __init__(self, lis):
        self.lis = lis
        self.num = 0

    def next(self):
        try:
            print(self.lis[self.num])
        except IndexError:
            print('List has no next item.')
        self.num += 1

    def peek(self):
        try:
            print(self.lis[self.num])
        except IndexError:
            print('List has no next item.')

    def hasNest(self):
        print('False') if self.num + 1 >= len(self.lis) else print('True')


if __name__ == '__main__':
    a = [1, 2, 4, 5, 6, 7, 8]
    b = Peeking_iterator(a)
    b.next()
    b.peek()
    b.next()
    b.next()
    b.hasNest()
    b.next()
    b.next()
    b.next()
    b.next()
    b.next()
    b.next()
    b.next()
    b.next()
    b.hasNest()
