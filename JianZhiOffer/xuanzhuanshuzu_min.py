# -*- coding: utf-8 -*-
"""
@author: MT
旋转数组的最小数字
题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
"""


def min_xuanzhuanshuzu(alist):
    if not alist:
        return
    start = 0
    end = len(alist) - 1

    if alist[start] < alist[end]:
        return alist[start]

    while start != end:
        mid = (start + end) / 2
        if mid == start:
            return alist[end]

        if alist[start] == alist[mid] == alist[end]:
            return min_in_order(alist, start, end)

        if alist[start] <= alist[mid]:
            start = mid
        elif alist[mid] <= alist[end]:
            end = mid
    return alist[end]


def min_in_order(alist, start, end):
    min_v = alist[start]
    for v in alist[start+1:end+1]:
        if v < min_v:
            min_v = v
    return min_v


if __name__ == '__main__':
    print min_xuanzhuanshuzu([5, 6, 7, 8, 9, 3, 4])
    print min_xuanzhuanshuzu([3, 3, 3, 3, 4, 5, 6, 7, 8, 2, 3, 3, 3, 3, 3])
    print min_xuanzhuanshuzu([3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
    print min_xuanzhuanshuzu([3, 2])
    print min_xuanzhuanshuzu([1, 0, 1, 1, 1])
    print min_xuanzhuanshuzu([1, 1, 1, 0, 1])
