# Given the head of a linked list, remove the nth node from the end of the list 
# and return its head. 
# 
#  Follow up: Could you do this in one pass? 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1], n = 1
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1,2], n = 1
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is sz. 
#  1 <= sz <= 30 
#  0 <= Node.val <= 100 
#  1 <= n <= sz 
#  
#  Related Topics 链表 双指针 
#  👍 1272 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     slow = fast = head
    #     for _ in range(n):
    #         fast = fast.next
    #     if not fast:
    #         return head.next
    #     while fast and fast.next:
    #         fast = fast.next
    #         slow = slow.next
    #     slow.next = slow.next.next
    #     return head

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        node = slow.next
        slow.next = node.next
        del node
        return head

# leetcode submit region end(Prohibit modification and deletion)
