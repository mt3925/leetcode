# Given a linked list, return the node where the cycle begins. If there is no cy
# cle, return null. 
# 
#  There is a cycle in a linked list if there is some node in the list that can 
# be reached again by continuously following the next pointer. Internally, pos is 
# used to denote the index of the node that tail's next pointer is connected to. N
# ote that pos is not passed as a parameter. 
# 
#  Notice that you should not modify the linked list. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the s
# econd node.
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the f
# irst node.
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of the nodes in the list is in the range [0, 104]. 
#  -105 <= Node.val <= 105 
#  pos is -1 or a valid index in the linked-list. 
#  
# 
#  
#  Follow up: Can you solve it using O(1) (i.e. constant) memory? 
#  Related Topics 链表 双指针 
#  👍 909 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def detectCycle(self, head: ListNode) -> ListNode:
    #     slow = fast = head
    #
    #     while 1:
    #         if not fast or not fast.next:
    #             return
    #         slow = slow.next
    #         fast = fast.next.next
    #         if slow == fast:
    #             break
    #     fast = head
    #     while fast != slow:
    #         fast = fast.next
    #         slow = slow.next
    #     return slow

    def detectCycle(self, head: ListNode) -> ListNode:

        slow = fast = head
        has_cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast and slow == fast:
                has_cycle = True
                break
        if not has_cycle:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

        
# leetcode submit region end(Prohibit modification and deletion)
