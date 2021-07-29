# Given a blacklist B containing unique integers from [0, N), write a function t
# o return a uniform random integer from [0, N) which is NOT in B. 
# 
#  Optimize it such that it minimizes the call to system’s Math.random(). 
# 
#  Note: 
# 
#  
#  1 <= N <= 1000000000 
#  0 <= B.length < min(100000, N) 
#  [0, N) does NOT include N. See interval notation. 
#  
# 
#  Example 1: 
# 
#  
# Input: 
# ["Solution","pick","pick","pick"]
# [[1,[]],[],[],[]]
# Output: [null,0,0,0]
#  
# 
#  Example 2: 
# 
#  
# Input: 
# ["Solution","pick","pick","pick"]
# [[2,[]],[],[],[]]
# Output: [null,1,1,1]
#  
# 
#  Example 3: 
# 
#  
# Input: 
# ["Solution","pick","pick","pick"]
# [[3,[1]],[],[],[]]
# Output: [null,0,0,2]
#  
# 
#  Example 4: 
# 
#  
# Input: 
# ["Solution","pick","pick","pick"]
# [[4,[2]],[],[],[]]
# Output: [null,1,3,1]
#  
# 
#  Explanation of Input Syntax: 
# 
#  The input is two lists: the subroutines called and their arguments. Solution'
# s constructor has two arguments, N and the blacklist B. pick has no arguments. A
# rguments are always wrapped with a list, even if there aren't any. 
#  Related Topics 排序 哈希表 二分查找 Random 
#  👍 57 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import random


# class Solution:
#
#     def __init__(self, N: int, blacklist: List[int]):
#         query_map = {}
#         rest_len = N - len(blacklist)
#         bl_set = set(blacklist)
#         right = N - 1
#         for item in blacklist:
#             if item < rest_len:
#                 while right in bl_set:
#                     right -= 1
#                 query_map[item] = right
#                 right -= 1
#         self.query_map = query_map
#         self.len = rest_len
#
#     def pick(self) -> int:
#         idx = int(random.random() * self.len)
#         return self.query_map.get(idx, idx)


class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.data_map = {}
        self.len = N - len(blacklist)
        last = N - 1
        bl_set = set(blacklist)
        for num in blacklist:
            if num < self.len:
                while last in bl_set:
                    last -= 1
                if last < self.len:
                    break
                self.data_map[num] = last
                last -= 1

    def pick(self) -> int:
        idx = random.randint(0, self.len - 1)
        return self.data_map.get(idx, idx)


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
# leetcode submit region end(Prohibit modification and deletion)
