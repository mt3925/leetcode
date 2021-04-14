# Given an array of intervals where intervals[i] = [starti, endi], merge all ove
# rlapping intervals, and return an array of the non-overlapping intervals that co
# ver all the intervals in the input. 
# 
#  
#  Example 1: 
# 
#  
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#  
# 
#  Example 2: 
# 
#  
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= intervals.length <= 104 
#  intervals[i].length == 2 
#  0 <= starti <= endi <= 104 
#  
#  Related Topics 排序 数组 
#  👍 847 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        rst = []
        for item in intervals:
            if not rst:
                rst.append(item)
                continue
            last = rst[-1]
            if item[0] <= last[1]:
                if item[1] > last[1]:
                    last[1] = item[1]
            else:
                rst.append(item)
        return rst


# leetcode submit region end(Prohibit modification and deletion)
