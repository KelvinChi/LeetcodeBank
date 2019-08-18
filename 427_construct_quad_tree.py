#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-05-14 07:23:57


class Node4:
    def __init__(self, value=None, b1=None, b2=None, b3=None, b4=None, isLeaf='Yes'):
        self.value = value
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.isLeaf = isLeaf

    def __str__(self):
        return str(self.value)


class Tree:
    lt = []
    lis = []

    def __init__(self):
        self.root = None

    def add(self, number):
        node = Node4(number)
        if self.root is None:
            self.root = node
            Tree.lt.append(self.root)
        else:
            while True:
                point = Tree.lt[0]
                if point.b1 is None:
                    point.b1 = node
                    point.isLeaf = 'No'
                    Tree.lt.append(point.b1)
                    return
                elif point.b2 is None:
                    point.b2 = node
                    point.isLeaf = 'No'
                    Tree.lt.append(point.b2)
                    return
                elif point.b3 is None:
                    point.b3 = node
                    point.isLeaf = 'No'
                    Tree.lt.append(point.b3)
                    return
                elif point.b4 is None:
                    point.b4 = node
                    point.isLeaf = 'No'
                    Tree.lt.append(point.b4)
                    Tree.lt.pop(0)
                    return

    def get_banches(self, root):
        if root is None:
            return
        print(root, root.isLeaf, end=' ')
        self.get_banches(root.b1)
        self.get_banches(root.b2)
        self.get_banches(root.b3)
        self.get_banches(root.b4)



if __name__ == '__main__':
    t = Tree()
    a = [3, 9, 1, 2, 5, 6, 8, 9, 4, 7, 3, 7, 9, 1, 4,
         7, 9, 9, 0, 3, 2, 7, 9, 0, 1, 3, 6, 3, 5, 9, 0]
    for i in a:
        t.add(i)
    t.get_banches(t.root)
