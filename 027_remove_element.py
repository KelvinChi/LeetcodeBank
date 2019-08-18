#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def re(nums, val):
    a = len(nums)
    pin = 0
    for i in range(a):
        if nums[i - pin] == val:
            nums.remove(nums[i - pin])
            pin += 1
    # while '' in nums:
    #     nums.remove('')
    return len(nums), nums


nums = [3, 2, 2, 2, 3]
val = 3
result = re(nums, val)
print(result)