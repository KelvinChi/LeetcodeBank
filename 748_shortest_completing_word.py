#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# import pysnooper


# @pysnooper.snoop()
def scw(licensePlate, words):
    temp = list(licensePlate)
    newPlate = []
    for i in temp:
        if i.isdigit() or i == ' ':
            pass
        else:
            newPlate.append(i.lower())
    print(newPlate)
    length = len(newPlate)
    final_list = []
    for j in words:
        pin = 0
        lis = list(j)
        for x in newPlate:
            if x not in lis:
                break
            else:
                lis.remove(x)
                pin += 1
                if pin == length:
                    final_list.append(j)
    if final_list:
        print(final_list)
        if len(final_list) == 1:
            return final_list[0]
        shortest = []
        for x in range(len(final_list) - 1):
            if len(final_list[x]) > len(final_list[x + 1]):
                if shortest:
                    shortest.pop()
                shortest.append(final_list[x + 1])
            else:
                pass
        return shortest[0]
    else:
        return -1


words = ["step", "steps", "stripe", "stepple"]
licensePlate = '1s3 PSt'
print(scw(licensePlate, words))
words = ["looks", "pest", "stew", "show"]
licensePlate = '1s3 456'
print(scw(licensePlate, words))