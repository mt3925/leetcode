# There are some spherical balloons spread in two-dimensional space. For each ba
# lloon, provided input is the start and end coordinates of the horizontal diamete
# r. Since it's horizontal, y-coordinates don't matter, and hence the x-coordinate
# s of start and end of the diameter suffice. The start is always smaller than the
#  end. 
# 
#  An arrow can be shot up exactly vertically from different points along the x-
# axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x 
# ≤ xend. There is no limit to the number of arrows that can be shot. An arrow onc
# e shot keeps traveling up infinitely. 
# 
#  Given an array points where points[i] = [xstart, xend], return the minimum nu
# mber of arrows that must be shot to burst all balloons. 
# 
#  
#  Example 1: 
# 
#  
# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: One way is to shoot one arrow for example at x = 6 (bursting the 
# balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two ba
# lloons).
#  
# 
#  Example 2: 
# 
#  
# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
#  
# 
#  Example 3: 
# 
#  
# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= points.length <= 104 
#  points[i].length == 2 
#  -231 <= xstart < xend <= 231 - 1 
#  
#  Related Topics 贪心算法 排序 
#  👍 388 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        end = points[0][1]
        cnt = 1
        for item in points[1:]:
            if item[0] > end:
                cnt += 1
                end = item[1]
        return cnt

# leetcode submit region end(Prohibit modification and deletion)
