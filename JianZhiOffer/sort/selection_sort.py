"""
选择排序的原理：每次在无序队列中“选择”出最小值，放到有序队列的最后，并从无序队列
  中去除该值（具体实现略有区别）。
"""


def selection_sort(alist):

    l_len = len(alist)
    for i in xrange(l_len - 1):
        min_idx = i
        for j in xrange(i + 1, l_len):
            if alist[j] < alist[min_idx]:
                min_idx = j
        if min_idx != i:
            alist[i], alist[min_idx] = alist[min_idx], alist[i]

    assert alist == sorted(alist)
    return alist


print selection_sort([
    2, 4, 56, 4, 456, 23, 34, 4564, 2, 343, 345, 3, 3453, 343, 3, 2, 45, 34,
    45, 34, 5, 456
])
