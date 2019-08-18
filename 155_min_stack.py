#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


class stack:
    def __init__(self, lis):
        if lis.__class__.__name__ == 'list':
            self.lis = lis
        else:
            print('type wrong')

    def push(self, num):
        self.lis.append(num)

    def pop(self):
        self.lis.pop()

    def top(self):
        print(self.lis[-1])

    def getMin(self):
        print(min(self.lis))

    def show(self):
        print(self.lis)

a = []
b = stack(a)
b.show()
b.push(-2)
b.push(0)
b.push(-3)
b.show()
b.top()
b.getMin()
b.pop()
b.top()
b.getMin()