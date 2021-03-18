# Given a string s, remove duplicate letters so that every letter appears once a
# nd only once. You must make sure your result is the smallest in lexicographical 
# order among all possible results. 
# 
#  Note: This question is the same as 1081: https://leetcode.com/problems/smalle
# st-subsequence-of-distinct-characters/ 
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
#  1 <= s.length <= 104 
#  s consists of lowercase English letters. 
#  
#  Related Topics 栈 贪心算法 字符串 
#  👍 483 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt_map = collections.Counter(s)

        seen = set()
        stack = []

        for item in s:
            if item in seen:
                cnt_map[item] -= 1
                continue
            while stack and cnt_map[stack[-1]] > 0 and ord(stack[-1]) > ord(item):
                seen.remove(stack.pop())
            stack.append(item)
            seen.add(item)
            cnt_map[item] -= 1
        return ''.join(stack)

# leetcode submit region end(Prohibit modification and deletion)
