# -*- coding: utf-8 -*-
"""
@author: MT
"""
import random


def test(func):
    for l in [random.randint(10, 20) for _ in range(5)]:
        alist = [random.randint(0, 1000) for _ in range(l)]
        print alist
        alist = func(alist)
        print alist
        assert alist == sorted(alist)

    assert func([]) == []
    assert func([3]) == [3]
