"""
冒泡排序的原理：每次在无序队列里将相邻两个数依次进行比较，将小数调换到前面，
  逐次比较，直至将最大的数移到最后。最将剩下的N-1个数继续比较，将次大数移至倒数第二位。
  依此规律，直至比较结束。
改进的冒泡排序, 加入一个校验, 如果某次循环发现没有发生数值交换, 直接跳出循环
"""


def bubble_sort(a_list):
    if not a_list:
        return a_list

    for tmp_len in xrange(len(a_list), 1, -1):
        exchange = False
        for i in xrange(1, tmp_len):
            if a_list[i - 1] > a_list[i]:
                a_list[i - 1], a_list[i] = a_list[i], a_list[i - 1]
                exchange = True
        if not exchange:
            break
    return a_list


print bubble_sort([2, 4, 56, 4, 456, 23, 34, 4564, 2, 343, 345, 3, 3453, 343, 3, 2, 45, 34, 45, 34, 5, 456])
print bubble_sort([])
print bubble_sort([1])
print bubble_sort([12, 4])

print range(1, 0)
print range(1, 1)
print range(5, 1, -1)
