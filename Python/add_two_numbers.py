"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it
 as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def add_next(self, x):
        self.next = x
        return self

    def __str__(self):
        n = self
        s = ''
        while n:
            s += str(n.val) + '->'
            n = n.next
        return s


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rtn, carry = l1, 0
        pre = cur = rtn
        while l1 and l2:
            carry, cur.val = divmod(l1.val + l2.val + carry, 10)
            l1, l2, pre, cur = l1.next, l2.next, cur, cur.next
        if l2:
            pre.next = cur = l2
        while carry:
            if not cur:
                pre.next = ListNode(carry)
                break
            carry, cur.val = divmod(cur.val + carry, 10)
            pre, cur = cur, cur.next
        return rtn


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(9).add_next(ListNode(9))
    print(l1)
    print(l2)
    print(Solution().addTwoNumbers(l1, l2))
