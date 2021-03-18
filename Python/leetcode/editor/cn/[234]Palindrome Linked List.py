# Given a singly linked list, determine if it is a palindrome. 
# 
#  Example 1: 
# 
#  
# Input: 1->2
# Output: false 
# 
#  Example 2: 
# 
#  
# Input: 1->2->2->1
# Output: true 
# 
#  Follow up: 
# Could you do it in O(n) time and O(1) space? 
#  Related Topics 链表 双指针 
#  👍 875 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         if not head:
#             return True
#         p = q = head
#         while q and q.next:
#             p = p.next
#             q = q.next.next
#
#         mid = p
#         q = p.next
#         while p and q:
#             tmp = q.next
#             q.next = p
#             p = q
#             q = tmp
#
#         while head != mid:
#             if head.val != p.val:
#                 return False
#             head = head.next
#             p = p.next
#         return True


# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         left = head
#
#         def _is_palindrome(root):
#             if not root:
#                 return True
#             res = _is_palindrome(root.next)
#             nonlocal left
#             res = res and (root.val == left.val)
#             left = left.next
#             return res
#         return _is_palindrome(head)


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        slow = fast = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev:
            if rev.val != slow.val:
                return False
            rev = rev.next
            slow = slow.next
        return True


# leetcode submit region end(Prohibit modification and deletion)
