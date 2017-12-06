"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def _add(node, v):
            _x, y = divmod(v, 10)
            node.val = y
            return _x
        
        _a, a, b = l1, l1, l2
        x = 0
        while a is not None and b is not None:
            _a, x, a, b = a, _add(a, a.val + b.val + x), a.next, b.next
        while a is not None and x is not 0:
            _a, x, a = a, _add(a, a.val + x), a.next
        while b is not None:
            if _a is None:
                _a = l1 = b
            else:
                _a.next = b
                _a = b
            x, b = _add(b, b.val + x), b.next
            if x is 0:
                break
        if x is not 0:
            _a.next = ListNode(x)
        return l1
