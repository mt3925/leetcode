# -*- coding: utf-8 -*-
"""
@author: MT
"""
import math


def merge_sort1(alist):
    """自顶向下归并"""
    if len(alist) <= 1:
        return alist

    def merge(alist, start, mid, end):
        aux = [x for x in alist[start:end + 1]]
        i = 0
        aux_mid = mid - start
        aux_end = end - start
        j = aux_mid + 1
        for idx in xrange(start, end + 1):
            if i > aux_mid:
                alist[idx] = aux[j]
                j += 1
            elif j > aux_end:
                alist[idx] = aux[i]
                i += 1
            elif aux[i] < aux[j]:
                alist[idx] = aux[i]
                i += 1
            else:
                alist[idx] = aux[j]
                j += 1

    def _merge_sort1(alist, start, end):
        if start == end:
            return
        mid = (start + end) / 2
        _merge_sort1(alist, start, mid)
        _merge_sort1(alist, mid + 1, end)
        merge(alist, start, mid, end)

    _merge_sort1(alist, 0, len(alist) - 1)


def merge_sort2(alist):
    if len(alist) <= 1:
        return alist

    mid = len(alist) / 2
    left = merge_sort2(alist[:mid])
    right = merge_sort2(alist[mid:])

    def merge(left, right):
        merged = []
        while left and right:
            merged.append(left.pop(0) if left[0] < right[0] else right.pop(0))
        merged.extend(left if left else right)
        return merged

    return merge(left, right)


def merge_sort3(alist):
    """自底向上归并"""

    def merge(left, right):
        merged = []
        while left and right:
            merged.append(left.pop(0) if left[0] < right[0] else right.pop(0))
        merged.extend(left if left else right)
        return merged

    n = len(alist)
    for i in range(0, int(math.ceil(n**0.5))):
        sz = 2**i
        start = 0
        while start < n:
            mid = start + sz
            end = min(start + sz * 2, n)
            alist[start:end] = merge(alist[start:mid], alist[mid:end])
            start = end
    return alist
