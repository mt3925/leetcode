# Given two strings s1 and s2, write a function to return true if s2 contains th
# e permutation of s1. In other words, one of the first string's permutations is t
# he substring of the second string. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
#  
# 
#  Example 2: 
# 
#  
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
#  
# 
#  
#  Constraints: 
# 
#  
#  The input strings only contain lower case letters. 
#  The length of both given strings is in range [1, 10,000]. 
#  
#  Related Topics 双指针 Sliding Window 
#  👍 324 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         need = collections.Counter(s1)
#         s1_len = len(s1)
#         s2_len = len(s2)
#         need_len = s1_len
#
#         if s1_len > s2_len:
#             return False
#
#         left = 0
#
#         for right in range(s1_len):
#             if need[s2[right]] > 0:
#                 need_len -= 1
#             need[s2[right]] -= 1
#             if need_len == 0:
#                 return True
#
#         for right in range(s1_len, s2_len):
#             need[s2[left]] += 1
#             if need[s2[left]] > 0:
#                 need_len += 1
#             left += 1
#
#             if need[s2[right]] > 0:
#                 need_len -= 1
#             need[s2[right]] -= 1
#             if need_len == 0:
#                 return True
#         return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ori_need = collections.Counter(s1)
        need = dict(ori_need.items())
        s1_len = len(s1)
        s2_len = len(s2)
        need_len = s1_len

        left = right = 0
        while right < s2_len:
            c = s2[right]
            if c in need:
                if need[c] > 0:
                    need_len -= 1
                    need[c] -= 1
                    right += 1
                    if need_len == 0:
                        return True
                else:
                    while left <= right and s2[left] != c:
                        need[s2[left]] += 1
                        need_len += 1
                        left += 1
                    left += 1
                    right += 1
            else:
                right += 1
                left = right
                need = dict(ori_need.items())
                need_len = s1_len
        return False

# leetcode submit region end(Prohibit modification and deletion)

# if __name__ == '__main__':
#     print(Solution().checkInclusion('ab', 'a'))
