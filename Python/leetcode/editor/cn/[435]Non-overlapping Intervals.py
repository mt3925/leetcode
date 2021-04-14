# Given an array of intervals intervals where intervals[i] = [starti, endi], ret
# urn the minimum number of intervals you need to remove to make the rest of the i
# ntervals non-overlapping. 
# 
#  
#  Example 1: 
# 
#  
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overla
# pping.
#  
# 
#  Example 2: 
# 
#  
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals no
# n-overlapping.
#  
# 
#  Example 3: 
# 
#  
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're alrea
# dy non-overlapping.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= intervals.length <= 2 * 104 
#  intervals[i].length == 2 
#  -2 * 104 <= starti < endi <= 2 * 104 
#  
#  Related Topics 贪心算法 
#  👍 400 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        cnt = 1
        for item in intervals[1:]:
            if item[0] >= end:
                cnt += 1
                end = item[1]
        return len(intervals) - cnt

# leetcode submit region end(Prohibit modification and deletion)
