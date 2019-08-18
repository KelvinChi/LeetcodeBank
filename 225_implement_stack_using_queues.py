#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


class Stack:
    def __init__(self, lis):
        self.lis = lis

    def show(self):
        return self.lis

    def push(self, num):
        self.lis.append(num)

    def pop(self):
        if self.lis:
            self.lis.pop()
        else:
            print('list can not be empty')

    def top(self):
        if self.lis:
            print(self.lis[-1])
        else:
            print('list can not be empty')

    def empty(self):
        print('False') if self.lis else print('True')


a = []
b = Stack(a)
b.push(1)
b.push(2)
b.top()
b.pop()
print(b.show())
b.empty()
