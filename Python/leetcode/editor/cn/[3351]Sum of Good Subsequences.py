# You are given an integer array nums. A good subsequence is defined as a 
# subsequence of nums where the absolute difference between any two consecutive 
# elements in the subsequence is exactly 1. 
# 
#  Return the sum of all possible good subsequences of nums. 
# 
#  Since the answer may be very large, return it modulo 10⁹ + 7. 
# 
#  Note that a subsequence of size 1 is considered good by definition. 
# 
#  
#  Example 1: 
# 
#  
#  Input: nums = [1,2,1] 
#  
# 
#  Output: 14 
# 
#  Explanation: 
# 
#  
#  Good subsequences are: [1], [2], [1], [1,2], [2,1], [1,2,1]. 
#  The sum of elements in these subsequences is 14. 
#  
# 
#  Example 2: 
# 
#  
#  Input: nums = [3,4,5] 
#  
# 
#  Output: 40 
# 
#  Explanation: 
# 
#  
#  Good subsequences are: [3], [4], [5], [3,4], [4,5], [3,4,5]. 
#  The sum of elements in these subsequences is 40. 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  0 <= nums[i] <= 10⁵ 
#  
# 
#  👍 11 👎 0
from typing import List
from collections import defaultdict


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:

        """
        动态规划
        f[x] 表示以x结尾的子序列的元素和
        cnt[x] 表示以x结尾的子序列的个数

        不选x，则元素和为f[x]
        选x
            x加在所有x-1结尾的子序列后，则这些子序列之和为 f[x-1] + cnt[x-1] * x
            x加载所有x+1结尾的子序列后，则这些子序列之和为 f[x+1] + cnt[x+1] * x
            x本身作为一个序列，元素和为x
        所以
        f[x] = f[x] + f[x-1] + f[x+1] + x(cnt[x-1] + cnt[x+1] + 1)
        cnt[x] = cnt[x] + cnt[x-1] + cnt[x+1] + 1
        """
        mod = 10 ** 9 + 7
        f = defaultdict(int)
        cnt = defaultdict(int)
        for x in nums:
            c = cnt[x-1] + cnt[x+1] + 1
            f[x] += f[x-1] + f[x+1] + x * c
            cnt[x] += c
        return sum(f.values()) % mod

        # # 回溯暴力解法
        # rst = []
        # n = len(nums)
        #
        # def back_trace(tmp, idx):
        #     if idx >= n:
        #         if tmp:
        #             rst.append(tmp[:])
        #         return
        #     if not tmp or abs(tmp[-1] - nums[idx]) == 1:
        #         tmp.append(nums[idx])
        #         back_trace(tmp, idx + 1)
        #         tmp.pop()
        #     back_trace(tmp, idx + 1)
        #
        # back_trace([], 0)
        # return sum([sum(i) for i in rst]) % (10 ** 9 + 7)

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().sumOfGoodSubsequences([1, 2, 1]))
    print(Solution().sumOfGoodSubsequences([3, 4, 5]))
