# Median is the middle value in an ordered integer list. If the size of the list
#  is even, there is no middle value. So the median is the mean of the two middle 
# value. 
# For example,
# 
#  [2,3,4], the median is 3 
# 
#  [2,3], the median is (2 + 3) / 2 = 2.5 
# 
#  Design a data structure that supports the following two operations: 
# 
#  
#  void addNum(int num) - Add a integer number from the data stream to the data 
# structure. 
#  double findMedian() - Return the median of all elements so far. 
#  
# 
#  
# 
#  Example: 
# 
#  
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
#  
# 
#  
# 
#  Follow up: 
# 
#  
#  If all integer numbers from the stream are between 0 and 100, how would you o
# ptimize it? 
#  If 99% of all integer numbers from the stream are between 0 and 100, how woul
# d you optimize it? 
#  
#  Related Topics 堆 设计 
#  👍 375 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class MedianFinder:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.min_pq = MinPriorityQueue()
#         self.max_pq = MaxPriorityQueue()
#
#     def addNum(self, num: int) -> None:
#         min_pq_min = self.min_pq.get_min()
#         if min_pq_min is None or num > min_pq_min:
#             self.min_pq.insert(num)
#             if self.min_pq.size - self.max_pq.size > 1:
#                 self.max_pq.insert(self.min_pq.del_min())
#         else:
#             self.max_pq.insert(num)
#             if self.max_pq.size - self.min_pq.size > 1:
#                 self.min_pq.insert(self.max_pq.del_max())
#
#     def findMedian(self) -> float:
#         if not self.min_pq.size and not self.max_pq.size:
#             return 0
#         if self.min_pq.size == self.max_pq.size:
#             return (self.max_pq.get_max() + self.min_pq.get_min()) / 2
#         elif self.min_pq.size > self.max_pq.size:
#             return self.min_pq.get_min()
#         else:
#             return self.max_pq.get_max()
#
#
# def parent(root):
#     if root == 0:
#         return 0
#     return (root - 1) // 2
#
#
# def left(root):
#     return root * 2 + 1
#
#
# def right(root):
#     return root * 2 + 2
#
#
# class MinPriorityQueue:
#     """优先队列"""
#
#     def __init__(self):
#         self._data = []
#         self.size = 0
#
#     def swim(self, node_idx):
#         parent_idx = parent(node_idx)
#         if parent_idx == node_idx:
#             return
#         parent_v = self._data[parent_idx]
#         node_v = self._data[node_idx]
#         if parent_v <= node_v:
#             return
#         self._data[parent_idx], self._data[node_idx] = node_v, parent_v
#         return self.swim(parent_idx)
#
#     def sink(self, node_idx):
#         left_idx = left(node_idx)
#         right_idx = right(node_idx)
#         if left_idx >= self.size:
#             return
#         compare_idx = left_idx
#         compare_val = self._data[left_idx]
#         if right_idx < self.size:
#             right_val = self._data[right_idx]
#             if right_val < compare_val:
#                 compare_idx = right_idx
#                 compare_val = right_val
#
#         node_val = self._data[node_idx]
#         if compare_val >= node_val:
#             return
#         self._data[node_idx], self._data[compare_idx] = compare_val, node_val
#         return self.sink(compare_idx)
#
#     def insert(self, value):
#         self._data.append(value)
#         self.swim(self.size)
#         self.size += 1
#
#     def del_min(self):
#         if not self._data:
#             return
#         min_val = self._data[0]
#         end_val = self._data.pop()
#         if self._data:
#             self._data[0] = end_val
#         self.size -= 1
#         self.sink(0)
#         return min_val
#
#     def get_min(self):
#         if not self._data:
#             return
#         return self._data[0]
#
#
# class MaxPriorityQueue:
#     """优先队列"""
#
#     def __init__(self):
#         self._data = []
#         self.size = 0
#
#     def swim(self, node_idx):
#         parent_idx = parent(node_idx)
#         if parent_idx == node_idx:
#             return
#         parent_v = self._data[parent_idx]
#         node_v = self._data[node_idx]
#         if parent_v >= node_v:
#             return
#         self._data[parent_idx], self._data[node_idx] = node_v, parent_v
#         return self.swim(parent_idx)
#
#     def sink(self, node_idx):
#         left_idx = left(node_idx)
#         right_idx = right(node_idx)
#         if left_idx >= self.size:
#             return
#         compare_idx = left_idx
#         compare_val = self._data[left_idx]
#         if right_idx < self.size:
#             right_val = self._data[right_idx]
#             if right_val > compare_val:
#                 compare_idx = right_idx
#                 compare_val = right_val
#
#         node_val = self._data[node_idx]
#         if compare_val <= node_val:
#             return
#         self._data[node_idx], self._data[compare_idx] = compare_val, node_val
#         return self.sink(compare_idx)
#
#     def insert(self, value):
#         self._data.append(value)
#         self.swim(self.size)
#         self.size += 1
#
#     def del_max(self):
#         if not self._data:
#             return
#         _val = self._data[0]
#         end_val = self._data.pop()
#         if self._data:
#             self._data[0] = end_val
#         self.size -= 1
#         self.sink(0)
#         return _val
#
#     def get_max(self):
#         if not self._data:
#             return
#         return self._data[0]


from heapq import *


class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# leetcode submit region end(Prohibit modification and deletion)


# if __name__ == '__main__':
#     obj = MedianFinder()
#     obj.addNum(1)
#     obj.addNum(2)
#     obj.addNum(3)
#     obj.addNum(4)
#     print(obj.findMedian())
