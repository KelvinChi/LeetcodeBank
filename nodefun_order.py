#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-04-11 04:43:20
# import pysnooper
# import sys
# sys.setrecursionlimit(1500)


class Node:
    def __init__(self, value=None, left=None, right=None, father=None):
        self.value = value
        self.left = left
        self.right = right
        self.father = father

    def __str__(self):
        return str(self.value)


class Tree:

    # lt = []

    def __init__(self):
        self.root = None
        self.lt = []

    def add(self, number):
        node = Node(number)
        if self.root is None:
            self.root = node
            self.lt.append(self.root)
            self.root.father = None
        else:
            while True:
                point = self.lt[0]
                if point.left is None:
                    point.left = node
                    self.lt.append(point.left)
                    point.left.father = point
                    return
                elif point.right is None:
                    point.right = node
                    self.lt.append(point.right)
                    point.right.father = point
                    self.lt.pop(0)
                    return

    def order(self, root, action='null'):
        if not root:
            return
        # print(root)
        start = [root]
        temp = []
        result = [str(root)]
        temp1 = []
        while start:
            for i in start:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            if action == 'ascending':
                for j in temp:
                    temp1.append(str(j))
                temp1.sort()
                result.extend(temp1)
                temp1 = []
            elif action == 'descending':
                for j in temp:
                    temp1.append(str(j))
                temp1.sort(reverse=True)
                result.extend(temp1)
                temp1 = []
            elif action == 'null':
                for j in temp:
                    result.append(str(j))
            start = temp
            temp = []
        return result

    def ascending(self, root):
        get = self.order(root, action='ascending')
        newt = Tree()
        for r in get:
            if r != 'None':
                newt.add(int(r))
            else:
                newt.add(None)
        return newt.root

    def descending(self, root):
        get = self.order(root, action='descending')
        newt = Tree()
        for r in get:
            if r != 'None':
                newt.add(int(r))
            else:
                newt.add(None)
        return newt.root

    def null(self, root):
        get = self.order(root, action='null')
        newt = Tree()
        for r in get:
            if r != 'None':
                newt.add(int(r))
            else:
                newt.add(None)
        return newt.root

    def prop(self, root):
        if not root:
            return
        # print(root)
        start = [root]
        temp1 = []
        result = []
        while start:
            for i in start:
                if i.left:
                    temp1.append(i.left)
                    result.append((i.left))
                    # print(i.left)
                if i.right:
                    temp1.append(i.right)
                    result.append((i.right))
                    # print(i.right)
            start = temp1
            temp1 = []
        print(root)
        for x in result:
            print(x)


if __name__ == '__main__':
    t = Tree()
    a = [6, 2, 1, 5, 7, 9, 0, 3, 4, None, 8]
    for h in a:
        t.add(h)
    t.prop(t.root)

    print('~' * 10)

    temp = t.ascending(t.root)
    t.prop(temp)

    print('~' * 10)

    temp = t.descending(t.root)
    t.prop(temp)

    print('~' * 10)

    temp = t.null(t.root)
    t.prop(temp)

    print('~' * 10)

    # treesort = TreeSort(t.root)
    # ascending = treesort.ascending(t.root)
    # get = Tree()
    # for j in ascending:
    #     get.add(j)
    # get.prop(get.root)
    #
    # print('~' * 10)
