#!/usr/bin/env python3
# encoding: utf-8


from nodefun import Tree


class Lup:
    ans = 0

    def lup(self, root):

        def arrow(root):
            if root is None: return 0
            left_length = arrow(root.left)
            right_length = arrow(root.right)
            left_arrow = right_arrow = 0
            if str(root.left) != 'None' and root.value == root.left.value:
                left_arrow = left_length + 1
            if str(root.right) != 'None' and root.value == root.right.value:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow(root)
        return self.ans





t = Tree()
lis = [1, 1, 1, 1, 2, None, None, 1, None, 2, 3, None,
       None, None, None, 1, None, None, None, None, 2]
for i in lis:
    t.add(i)
print(Lup().lup(t.root))