# You are given an array of k linked-lists lists, each linked-list is sorted in 
# ascending order. 
# 
#  Merge all the linked-lists into one sorted linked-list and return it. 
# 
#  
#  Example 1: 
# 
#  
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
#  
# 
#  Example 2: 
# 
#  
# Input: lists = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: lists = [[]]
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  k == lists.length 
#  0 <= k <= 10^4 
#  0 <= lists[i].length <= 500 
#  -10^4 <= lists[i][j] <= 10^4 
#  lists[i] is sorted in ascending order. 
#  The sum of lists[i].length won't exceed 10^4. 
#  
#  Related Topics 堆 链表 分治算法 
#  👍 1197 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# import heapq
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         pq = []
#         rst_head = rst_tail = ListNode(None)
#
#         for idx, node in enumerate(lists):
#             if node:
#                 heapq.heappush(pq, (node.val, idx))
#
#         while pq:
#             _, idx = heapq.heappop(pq)
#             node = lists[idx]
#             rst_tail.next = node
#             rst_tail = node
#             if node.next:
#                 lists[idx] = node.next
#                 heapq.heappush(pq, (node.next.val, idx))
#         return rst_head.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        len_lists = len(lists)
        if len_lists == 1:
            return lists[0]
        mid = len_lists // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        head = tail = ListNode(None)
        while left and right:
            if left.val <= right.val:
                tail.next = left
                tail = left
                left = left.next
            else:
                tail.next = right
                tail = right
                right = right.next
        if left:
            tail.next = left
        if right:
            tail.next = right
        return head.next

# leetcode submit region end(Prohibit modification and deletion)
