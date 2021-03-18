# Write a function that reverses a string. The input string is given as an array
#  of characters char[]. 
# 
#  Do not allocate extra space for another array, you must do this by modifying 
# the input array in-place with O(1) extra memory. 
# 
#  You may assume all the characters consist of printable ascii characters. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#  
#  
#  
#  Related Topics 双指针 字符串 
#  👍 368 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
# leetcode submit region end(Prohibit modification and deletion)
