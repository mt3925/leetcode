# Given the head of a singly linked list and two integers left and right where l
# eft <= right, reverse the nodes of the list from position left to position right
# , and return the reversed list. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [5], left = 1, right = 1
# Output: [5]
#  
#
#
#  Constraints: 
# 
#  
#  The number of nodes in the list is n. 
#  1 <= n <= 500 
#  -500 <= Node.val <= 500 
#  1 <= left <= right <= n 
#  
# 
#  
# Follow up: Could you do it in one pass? Related Topics 链表 
#  👍 693 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
#         if not head:
#             return
#         num = 1
#         before_left = 0
#         rev = None
#         p = head
#         while p:
#             if left <= num <= right:
#                 if before_left is 0:
#                     before_left = rev
#                 rev, p.next, p = p, rev, p.next
#             elif num < left:
#                 rev, p = p, p.next
#             else:
#                 break
#             num += 1
#         if before_left:
#             if before_left.next:
#                 before_left.next.next = p
#                 before_left.next = rev
#         else:
#             head.next = p
#             head = rev
#         return head

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == 1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

    def reverseN(self, head, n):
        after_right = None
        def _reverseN(head, n):
            nonlocal after_right
            if n == 1:
                after_right = head.next
                return head

            last = _reverseN(head.next, n - 1)
            head.next.next = head
            head.next = after_right
            return last
        return _reverseN(head, n)


# leetcode submit region end(Prohibit modification and deletion)
