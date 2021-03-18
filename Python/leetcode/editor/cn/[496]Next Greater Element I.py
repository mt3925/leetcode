# You are given two integer arrays nums1 and nums2 both of unique elements, wher
# e nums1 is a subset of nums2. 
# 
#  Find all the next greater numbers for nums1's elements in the corresponding p
# laces of nums2. 
# 
#  The Next Greater Number of a number x in nums1 is the first greater number to
#  its right in nums2. If it does not exist, return -1 for this number. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation:
# For number 4 in the first array, you cannot find the next greater number for i
# t in the second array, so output -1.
# For number 1 in the first array, the next greater number for it in the second 
# array is 3.
# For number 2 in the first array, there is no next greater number for it in the
#  second array, so output -1. 
# 
#  Example 2: 
# 
#  
# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation:
# For number 2 in the first array, the next greater number for it in the second 
# array is 3.
# For number 4 in the first array, there is no next greater number for it in the
#  second array, so output -1. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums1.length <= nums2.length <= 1000 
#  0 <= nums1[i], nums2[i] <= 104 
#  All integers in nums1 and nums2 are unique. 
#  All the integers of nums1 also appear in nums2. 
#  
# 
#  
# Follow up: Could you find an O(nums1.length + nums2.length) solution? Related 
# Topics 栈 
#  👍 382 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        rst = {}
        stack = []

        for i in reversed(nums2):
            while stack:
                if i >= stack[-1]:
                    stack.pop()
                else:
                    break
            rst[i] = stack[-1] if stack else -1
            stack.append(i)
        return [rst.get(i) for i in nums1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
