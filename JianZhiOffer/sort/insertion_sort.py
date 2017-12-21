"""
  插入排序的原理：始终定义第一个元素为有序的，将元素逐个插入到有序排列之中，其特点是要不断的
  移动数据，空出一个适当的位置，把待插入的元素放到里面去。
"""


def insertion_sort(alist):
    for i in xrange(1, len(alist)):
        j = i - 1
        tmp = alist[i]
        while j >= 0 and alist[j] > tmp:
            alist[j + 1] = alist[j]
            j -= 1
        alist[j + 1] = tmp

    assert alist == sorted(alist)
    return alist


def insertion_sort2(alist):
    for i, v in enumerate(alist):
        pos = i
        while pos > 0 and alist[pos - 1] > v:
            alist[pos] = alist[pos - 1]
            pos -= 1
        alist[pos] = v

    assert alist == sorted(alist)
    return alist


print insertion_sort2([
    2, 4, 56, 4, 456, 23, 34, 4564, 2, 343, 345, 3, 3453, 343, 3, 2, 45, 34,
    45, 34, 5, 456
])
