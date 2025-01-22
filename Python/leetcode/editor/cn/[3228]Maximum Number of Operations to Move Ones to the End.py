# You are given a binary string s. 
# 
#  You can perform the following operation on the string any number of times: 
# 
#  
#  Choose any index i from the string where i + 1 < s.length such that s[i] == 
# '1' and s[i + 1] == '0'. 
#  Move the character s[i] to the right until it reaches the end of the string 
# or another '1'. For example, for s = "010010", if we choose i = 1, the resulting 
# string will be s = "000110". 
#  
# 
#  Return the maximum number of operations that you can perform. 
# 
#  
#  Example 1: 
# 
#  
#  Input: s = "1001101" 
#  
# 
#  Output: 4 
# 
#  Explanation: 
# 
#  We can perform the following operations: 
# 
#  
#  Choose index i = 0. The resulting string is s = "0011101". 
#  Choose index i = 4. The resulting string is s = "0011011". 
#  Choose index i = 3. The resulting string is s = "0010111". 
#  Choose index i = 2. The resulting string is s = "0001111". 
#  
# 
#  Example 2: 
# 
#  
#  Input: s = "00111" 
#  
# 
#  Output: 0 
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] is either '0' or '1'. 
#  
# 
#  👍 1 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        left = right = None
        rst = 0
        for i in range(0, n):
            if s[i] != '1':
                continue
            # 首次遇上1
            if left is None:
                left = right = i
            # 后续遇上1
            else:
                if right < i - 1:
                    rst += right - left + 1
                left += i - right - 1
                right = i
        if left is not None and right < n - 1:
            rst += right - left + 1
        return rst

# leetcode submit region end(Prohibit modification and deletion)


# if __name__ == '__main__':
#     print(Solution().maxOperations("1001101"))
#     print(Solution().maxOperations("00111"))
#     print(Solution().maxOperations("00"))
