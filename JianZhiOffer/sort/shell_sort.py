# -*- coding: utf-8 -*-
"""
@author: MT

希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
"""


def shell_sort(alist):
    n = len(alist)

    h = 1
    while h < n / 3:
        h = h * 3 + 1

    while h >= 1:
        # 将数组变为h有序
        for i in xrange(h, n):
            current_value = alist[i]
            j = i
            while j >= h and alist[j - h] > current_value:
                alist[j] = alist[j - h]
                j -= h
            alist[j] = current_value

        h = h / 3
    return alist
