#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


class Implement_queue_using_stacks:
    def __init__(self):
        self.lis = []

    def push(self, num):
        self.lis.append(num)

    def pop(self):
        del(self.lis[0])

    def peek(self):
        print(self.lis[0])

    def empty(self):
        if self.lis:
            print('False')
        else:
            print('True')

    def show(self):
        print(self.lis)


a = Implement_queue_using_stacks()
a.show()
a.push(7)
a.show()
a.push(1)
a.push(5)
a.push(7)
a.show()
a.pop()
a.show()
a.peek()
a.pop()
a.empty()
a.show()

