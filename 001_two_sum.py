#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def two_Sum(self):
        # 获取nums的序号列表
        keys = list(range(len(self.nums)))
        # 得到字典
        sum_dict = dict(zip(keys, self.nums))
        key_list = []
        for key, value in sum_dict.items():
            temp = self.target - int(sum_dict[key])
            if temp in sum_dict.values():
                key_list.append(key)
            else:
                pass
        if len(key_list) == 1:
            return None
        else:
            return key_list


def main():
    nums = [2, 7, 11, 15]
    target = 9
    x = Solution(nums, target)
    print(x.two_Sum())


if __name__ == '__main__':
    main()
