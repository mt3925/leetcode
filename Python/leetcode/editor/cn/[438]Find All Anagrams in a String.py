# Given a string s and a non-empty string p, find all the start indices of p's a
# nagrams in s. 
# 
#  Strings consists of lowercase English letters only and the length of both str
# ings s and p will not be larger than 20,100. 
# 
#  The order of output does not matter. 
# 
#  Example 1:
#  
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#  
#  
# 
#  Example 2:
#  
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#  
#  Related Topics 哈希表 
#  👍 490 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     if len(p) > len(s):
    #         return []
    #     need = collections.Counter(p)
    #     left, right = 0, len(p)
    #     window = collections.Counter(s[left: right])
    #     rst = []
    #     while right < len(s):
    #         if window == need:
    #             rst.append(left)
    #         window[s[right]] += 1
    #         window[s[left]] -= 1
    #         if not window[s[left]]:
    #             del window[s[left]]
    #         right += 1
    #         left += 1
    #     if window == need:
    #         rst.append(left)
    #     return rst

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        need = collections.Counter(p)
        p_len = len(p)
        need_len = len(p)
        left, right = 0, len(p)
        rst = []
        for right in range(len(s)):
            if right >= p_len:
                need[s[left]] += 1
                if need[s[left]] > 0:
                    need_len += 1
                left += 1

            if need[s[right]] > 0:
                need_len -= 1
            need[s[right]] -= 1
            if need_len == 0:
                rst.append(left)
        return rst


# leetcode submit region end(Prohibit modification and deletion)

# if __name__ == '__main__':
#     print(Solution().findAnagrams('cbaebabacd', 'abc'))
