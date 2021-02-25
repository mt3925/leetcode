"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a
 subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dict = dict()
        start = length = 0
        for idx, char in enumerate(s):
            rpt_char_idx = char_dict.get(char, -1)
            if rpt_char_idx >= start:
                tmp_len, start = idx - start, rpt_char_idx + 1
                if tmp_len > length:
                    length = tmp_len
            char_dict[char] = idx
        return max(length, len(s) - start)


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('dvdf'))
