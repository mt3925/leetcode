# Return the lexicographically smallest subsequence of s that contains all the d
# istinct characters of s exactly once. 
# 
#  Note: This question is the same as 316: https://leetcode.com/problems/remove-
# duplicate-letters/ 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "bcabc"
# Output: "abc"
#  
# 
#  Example 2: 
# 
#  
# Input: s = "cbacdcbc"
# Output: "acdb"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 1000 
#  s consists of lowercase English letters. 
#  
#  Related Topics 栈 贪心算法 字符串 
#  👍 88 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        idx_map = {i: idx for idx, i in enumerate(s)}
        seen = set()
        stack = ['!']
        for idx, item in enumerate(s):
            if item in seen:
                continue
            while idx_map.get(stack[-1], 0) > idx and ord(stack[-1]) > ord(item):
                seen.remove(stack.pop())
            stack.append(item)
            seen.add(item)
        return ''.join(stack[1:])


# leetcode submit region end(Prohibit modification and deletion)
