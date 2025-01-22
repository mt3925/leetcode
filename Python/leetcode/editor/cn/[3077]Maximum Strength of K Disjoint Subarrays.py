# You are given an array of integers nums with length n, and a positive odd 
# integer k. 
# 
#  Select exactly k disjoint subarrays sub1, sub2, ..., subk from nums such 
# that the last element of subi appears before the first element of sub{i+1} for all 1
#  <= i <= k-1. The goal is to maximize their combined strength. 
# 
#  The strength of the selected subarrays is defined as: 
# 
#  strength = k * sum(sub1)- (k - 1) * sum(sub2) + (k - 2) * sum(sub3) - ... - 2
#  * sum(sub{k-1}) + sum(subk) 
# 
#  where sum(subi) is the sum of the elements in the i-th subarray. 
# 
#  Return the maximum possible strength that can be obtained from selecting 
# exactly k disjoint subarrays from nums. 
# 
#  Note that the chosen subarrays don't need to cover the entire array. 
# 
#  
#  Example 1: 
# 
#  Input: nums = [1,2,3,-1,2], k = 3 
# 
#  Output: 22 
# 
#  Explanation: 
# 
#  The best possible way to select 3 subarrays is: nums[0..2], nums[3..3], and 
# nums[4..4]. The strength is calculated as follows: 
# 
#  strength = 3 * (1 + 2 + 3) - 2 * (-1) + 2 = 22 
# 
#  
# 
#  Example 2: 
# 
#  Input: nums = [12,-2,-2,-2,-2], k = 5 
# 
#  Output: 64 
# 
#  Explanation: 
# 
#  The only possible way to select 5 disjoint subarrays is: nums[0..0], nums[1..
# 1], nums[2..2], nums[3..3], and nums[4..4]. The strength is calculated as 
# follows: 
# 
#  strength = 5 * 12 - 4 * (-2) + 3 * (-2) - 2 * (-2) + (-2) = 64 
# 
#  Example 3: 
# 
#  Input: nums = [-1,-2,-3], k = 1 
# 
#  Output: -1 
# 
#  Explanation: 
# 
#  The best possible way to select 1 subarray is: nums[0..0]. The strength is -1
# . 
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10⁴ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  1 <= k <= n 
#  1 <= n * k <= 10⁶ 
#  k is odd. 
#  
# 
#  👍 24 👎 0


# from itertools import accumulate
from math import inf

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximumStrength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # # dp[i][j] 表示前j个数中选i个子数组的最大能量值
        # # dp[i][j] 不选择j-1 则 dp[i][j] = dp[i][j-1]
        # # 选择j-1作为第i个子数组的最右端元素，假设第i-1个子数组的最右端元素下标是p，则 dp[i][j] = dp[i-1][p] + （s[j] - s[p]）* w
        # # 其中w = -1**(i-1)(k-i+1)
        # # 所以dp[i][j] = max(dp[i][j-1], max([dp[i-1][p_min] + (s[j] - s[p_min]), ..., dp[i-1][p_max] + (s[j] - s[p_max]) * w])) p的范围为[i-1, j-1]
        # n = len(nums)
        # # 前缀和
        # s = list(accumulate(nums, initial=0))
        # dp = [[0] * (n + 1) for _ in range(k + 1)]
        # for i in range(1, k + 1):
        #     dp[i][i - 1] = mx = -inf
        #     w = (k - i + 1) * (1 if i % 2 else -1)
        #     # j 不能太小也不能太大，要给前面留 i-1 个数，后面留 k-i 个数
        #     for j in range(i, n - k + i + 1):
        #         mx = max(mx, dp[i - 1][j - 1] - s[j - 1] * w)
        #         dp[i][j] = max(dp[i][j - 1], mx + s[j] * w)
        # return dp[k][n]

        '''
        c(i, j) = nums[i-1] * (k + 1 - j) * (-1)**j 表示第i个元素在第j个子数组里贡献的能量值
        dp[i][j][1] 表示 第i个元素在第j个子数组里的最大能量值
        dp[i][j][0] 表示 第i个元素在第j个子数组后面不被选择的连续段里的最大能量值
        状态转移：
        第i个元素 不选，dp[i][j][0] = max(dp[i-1][j][1], dp[i-1][j][0])
        第i个元素 选，则两种可能：
            i和i-1在一个段里，dp[i][j][1] = dp[i-1][j][1] + c(i, j)
            i和i-1在不同的段里，也就是i新开一段，dp[i][j][1] = max(dp[i-1][j-1][0], dp[i-1][j-1][1]) + c(i, j)
        '''
        n = len(nums)
        dp = [[[-inf] * 2 for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(0, n + 1):
            dp[i][0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i + 1, k + 1)):
                dp[i][j][0] = max(dp[i-1][j])
                c = nums[i-1] * (k + 1 - j) * (1 if j % 2 else -1)
                dp[i][j][1] = max(dp[i-1][j][1] + c, max(dp[i-1][j-1]) + c)
        # print(dp)
        return max(dp[n][k])

        # # 优化空间
        # n = len(nums)
        # dp = [[-inf] * 2 for _ in range(k + 1)]
        # dp[0][0] = 0
        # for i in range(1, n + 1):
        #     for j in range(min(i, k), 0, -1):
        #         c = nums[i - 1] * (k + 1 - j) * (1 if j % 2 else -1)
        #         dp[j][1] = max(dp[j][1] + c, dp[j - 1][0] + c)
        #         dp[j][0] = max(dp[j])
        # # print(dp)
        # return dp[k][0]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().maximumStrength(nums=[1, 2, 3, -1, 2], k=3))
    print(Solution().maximumStrength(nums=[12, -2, -2, -2, -2], k=5))
    print(Solution().maximumStrength(nums=[-99, 85], k=1))
