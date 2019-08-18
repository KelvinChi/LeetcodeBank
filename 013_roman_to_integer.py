#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def translation(item):
    keys = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    values = [1000, 500, 100, 50, 10, 5, 1]
    dic = dict(zip(keys, values))
    return dic[item]



def get_num_list(original_list):
    num_list = []
    for i in original_list:
        num_list.append(translation(i))
    return num_list


def count(nums):
    length = len(nums)
    new_list = []
    for num in nums:
        for i in range(length):
            if i < length - 1:
                if 10 * (nums[i]) == nums[i + 1] or 5 * \
                        (nums[i]) == nums[i + 1]:
                    new_list.append(nums[i + 1] - nums[i])
                elif 10 * (nums[i - 1]) == nums[i] or 5 * (nums[i - 1]) == nums[i]:
                    pass
                else:
                    new_list.append(nums[i])
            else:
                if 10 * (nums[i - 1]) == nums[i] or 5 * \
                        (nums[i - 1]) == nums[i]:
                    pass
                else:
                    new_list.append(nums[i])
        return sum(new_list)


a = input('请输入4000内的罗马数字')
b = get_num_list(a)
c = count(b)
print(c)
