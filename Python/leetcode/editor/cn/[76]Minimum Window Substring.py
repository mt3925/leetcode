# Given two strings s and t, return the minimum window in s which will contain a
# ll the characters in t. If there is no such window in s that covers all characte
# rs in t, return the empty string "". 
# 
#  Note that If there is such a window, it is guaranteed that there will always 
# be only one unique minimum window in s. 
# 
#  
#  Example 1: 
#  Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
#  Example 2: 
#  Input: s = "a", t = "a"
# Output: "a"
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length, t.length <= 105 
#  s and t consist of English letters. 
#  
# 
#  
# Follow up: Could you find an algorithm that runs in O(n) time? Related Topics 
# 哈希表 双指针 字符串 Sliding Window 
#  👍 1025 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         window = collections.defaultdict(int)
#         need = collections.defaultdict(int)
#         for c in t:
#             need[c] += 1
#         need = list(need.items())
#
#         left = right = 0
#         rst_idx = 0
#         rst_len = 0
#         len_s = len(s)
#         window[s[left]] += 1
#         while 1:
#             if all([window.get(k, 0) >= v for k, v in need]):
#                 _len = right - left + 1
#                 if not rst_len or rst_len > _len:
#                     rst_idx = left
#                     rst_len = _len
#                 window[s[left]] -= 1
#                 left += 1
#             else:
#                 right += 1
#                 if right >= len_s:
#                     break
#                 window[s[right]] += 1
#         if rst_len:
#             return s[rst_idx: rst_idx + rst_len]
#         return ''


# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         need = collections.Counter(t)
#         target_len = len(t)
#
#         left = 0
#         rst_idx = 0
#         rst_len = 0
#         for right in range(len(s)):
#             if need[s[right]] > 0:
#                 target_len -= 1
#             need[s[right]] -= 1
#
#             while target_len == 0:
#                 _len = right - left + 1
#                 if not rst_len or rst_len > _len:
#                     rst_idx = left
#                     rst_len = _len
#
#                 need[s[left]] += 1
#                 if need[s[left]] > 0:
#                     target_len += 1
#                 left += 1
#         return s[rst_idx: rst_idx + rst_len] if rst_len else ''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_len = len(t)
        s_len = len(s)
        need = collections.Counter(t)

        left = right = 0
        rst_start = -1
        rst_len = s_len + 1
        while right < s_len:
            c = s[right]
            if need[c] > 0:
                need_len -= 1
            need[c] -= 1
            right += 1

            while need_len == 0:
                lc = s[left]
                need[lc] += 1
                if need[lc] > 0:
                    need_len += 1
                    if right - left < rst_len:
                        rst_start = left
                        rst_len = right - left
                left += 1
        if rst_start < 0:
            return ""
        return s[rst_start: rst_start+rst_len]

# leetcode submit region end(Prohibit modification and deletion)


# if __name__ == '__main__':
#     print(Solution().minWindow('ADOBECODEBANC', 'ABC'))
