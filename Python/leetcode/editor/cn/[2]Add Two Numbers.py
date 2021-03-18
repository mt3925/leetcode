# You are given two non-empty linked lists representing two non-negative integer
# s. The digits are stored in reverse order, and each of their nodes contains a si
# ngle digit. Add the two numbers and return the sum as a linked list. 
# 
#  You may assume the two numbers do not contain any leading zero, except the nu
# mber 0 itself. 
# 
#  
#  Example 1: 
# 
#  
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#  
# 
#  Example 2: 
# 
#  
# Input: l1 = [0], l2 = [0]
# Output: [0]
#  
# 
#  Example 3: 
# 
#  
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in each linked list is in the range [1, 100]. 
#  0 <= Node.val <= 9 
#  It is guaranteed that the list represents a number that does not have leading
#  zeros. 
#  
#  Related Topics 递归 链表 数学 
#  👍 5834 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     head = tmp = ListNode(None)
    #     extra = 0
    #     while l1 and l2:
    #         extra, val = divmod(l1.val + l2.val + extra, 10)
    #         tmp.next = ListNode(val)
    #         tmp = tmp.next
    #         l1 = l1.next
    #         l2 = l2.next
    #
    #     while l1:
    #         extra, val = divmod(l1.val + extra, 10)
    #         tmp.next = ListNode(val)
    #         tmp = tmp.next
    #         l1 = l1.next
    #
    #     while l2:
    #         extra, val = divmod(l2.val + extra, 10)
    #         tmp.next = ListNode(val)
    #         tmp = tmp.next
    #         l2 = l2.next
    #
    #     if extra:
    #         tmp.next = ListNode(extra)
    #     return head.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = pre = cur = l1
        extra = 0
        while cur and l2:
            extra, cur.val = divmod(cur.val + l2.val + extra, 10)
            pre = cur
            cur = cur.next
            l2 = l2.next

        if l2:
            pre.next = cur = l2
        while extra:
            if not cur:
                pre.next = ListNode(extra)
                break
            extra, cur.val = divmod(cur.val + extra, 10)
            pre = cur
            cur = cur.next
        return head
# leetcode submit region end(Prohibit modification and deletion)
