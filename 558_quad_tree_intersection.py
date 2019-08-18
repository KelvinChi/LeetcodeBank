#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK


class Node:
    def __init__(self, value=None, topLeft=None, topRight=None,
                 bottomLeft=None, bottomRight=None, isLeaf=None, level=None):
        self.value = value
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
        self.isLeaf = isLeaf
        self.level = level

    def __str__(self):
        return str(self.value)


class Tree:

    def __init__(self):
        self.root = None
        self.lt = []

    def add(self, mark):
        node = Node(mark)
        if self.root is None:
            self.root = node
            self.lt.append(self.root)
            self.root.isLeaf = True
            self.root.level = 0
        else:
            while True:
                point = self.lt[0]
                if point.topLeft is None:
                    point.topLeft = node
                    point.isLeaf = False
                    self.lt.append(point.topLeft)
                    point.topLeft.isLeaf = True
                    point.topLeft.level = point.level + 1
                    return
                elif point.topRight is None:
                    point.topRight = node
                    self.lt.append(point.topRight)
                    point.topRight.isLeaf = True
                    point.topRight.level = point.level + 1
                    return
                elif point.bottomLeft is None:
                    point.bottomLeft = node
                    self.lt.append(point.topRight)
                    point.bottomLeft.isLeaf = True
                    point.bottomLeft.level = point.level + 1
                    return
                elif point.bottomRight is None:
                    point.bottomRight = node
                    self.lt.append(point.bottomRight)
                    point.bottomRight.isLeaf = True
                    point.bottomRight.level = point.level + 1
                    if point.bottomRight.value == 'T' or point.bottomRight.value == 'F':
                        point.value = 'None'
                    self.lt.pop(0)
                    return

    def traverse_by_layer(self, root):
        if not root:
            return
        start = [root]
        temp = []
        result = [root]
        while start:
            for i in start:
                if i.topLeft:
                    temp.append(i.topLeft)
                    result.append(i.topLeft)
                if i.topRight:
                    temp.append(i.topRight)
                    result.append(i.topRight)
                if i.bottomLeft:
                    temp.append(i.bottomLeft)
                    result.append(i.bottomLeft)
                if i.bottomRight:
                    temp.append(i.bottomRight)
                    result.append(i.bottomRight)
            start = temp
            temp = []
        return result

    def prop(self, root):
        if root is None:
            return
        print('|    ' * root.level, '+--', root)
        self.prop(root.topLeft)
        self.prop(root.topRight)
        self.prop(root.bottomLeft)
        self.prop(root.bottomRight)


# def add_fun(t1, t2):
#     a = max(len(t1), len(t2))
#     count = 0
#     b = 1
#     while a > b:
#         count += 1
#         b = (4 ** (count + 1) - 1) / 3
#     t1_added = add_nones(t1, b)
#     t2_added = add_nones(t2, b)




# def add_nones(lis, length):
#     for i in range(len(lis), length):
#         lis.append('None')
#     return lis

def add_node(t1, t2):
    if t1 is None or t2 is None:
        return
    if str(t1.value) == str(t2.value):
        return t1
    elif str(t1.value) == 'None':
        return Node(str(t2.value), str(t2.value), str(t2.value), str(t2.value), str(t2.value))
    elif str(t2.value) == 'None':
        return Node(str(t1.value), str(t1.value), str(t1.value), str(t1.value), str(t1.value))
    else:
        t1.value = 'T'
        return t1


def add_tree(t1, t2):
    if t1 is None or t2 is None:
        return
    a = add_node(t1, t2)
    print(a)
    add_tree(t1.topLeft, t2.topLeft)
    add_tree(t1.topRight, t2.topRight)
    add_tree(t1.bottomLeft, t2.bottomLeft)
    add_tree(t1.bottomRight, t2.bottomRight)


if __name__ == '__main__':
    t1 = Tree()
    a = ['T', 'F', 'T', 'T', 'F', None, None, None, None, 'F', 'F', 'T', 'T']
    for i in a:
        t1.add(i)
    for x in t1.traverse_by_layer(t1.root):
        print(x.value)
    print('~' * 20)
    t2 = Tree()
    b = ['T', 'T', 'T', 'F', 'F']
    for j in b:
        t2.add(j)
    for y in t2.traverse_by_layer(t2.root):
        print(y.value)
    print('~' * 20)
    add_tree(t1.root, t2.root)




