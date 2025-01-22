# You are given an integer num. You know that Bob will sneakily remap one of 
# the 10 possible digits (0 to 9) to another digit. 
# 
#  Return the difference between the maximum and minimum values Bob can make by 
# remapping exactly one digit in num. 
# 
#  Notes: 
# 
#  
#  When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences 
# of d1 in num with d2. 
#  Bob can remap a digit to itself, in which case num does not change. 
#  Bob can remap different digits for obtaining minimum and maximum values 
# respectively. 
#  The resulting number after remapping can contain leading zeroes. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: num = 11891
# Output: 99009
# Explanation: 
# To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to 
# yield 99899.
# To achieve the minimum value, Bob can remap the digit 1 to the digit 0, 
# yielding 890.
# The difference between these two numbers is 99009.
#  
# 
#  Example 2: 
# 
#  
# Input: num = 90
# Output: 99
# Explanation:
# The maximum value that can be returned by the function is 99 (if 0 is 
# replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is 
# replaced by 0).
# Thus, we return 99. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= num <= 10⁸ 
#  
# 
#  👍 22 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minMaxDifference(self, num: int) -> int:
        tmp = num
        nums = []
        while tmp:
            tmp, mod = divmod(tmp, 10)
            nums.append(mod)

        max_remap = None
        min_remap = None
        rst = 0
        for i in nums[::-1]:
            if i != 9 and max_remap is None:
                max_remap = i
            if min_remap is None:
                min_remap = i

            max_i = 9 if i == max_remap else i
            min_i = 0 if i == min_remap else i
            rst = rst * 10 + max_i - min_i
        return rst

# leetcode submit region end(Prohibit modification and deletion)

#
# if __name__ == '__main__':
#     print(Solution().minMaxDifference(11891))
#     print(Solution().minMaxDifference(90))
