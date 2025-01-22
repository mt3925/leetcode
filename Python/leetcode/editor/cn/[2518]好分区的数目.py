# 给你一个正整数数组 nums 和一个整数 k 。 
# 
#  分区 的定义是：将数组划分成两个有序的 组 ，并满足每个元素 恰好 存在于 某一个 组中。如果分区中每个组的元素和都大于等于 k ，则认为分区是一个好分区
# 。 
# 
#  返回 不同 的好分区的数目。由于答案可能很大，请返回对 10⁹ + 7 取余 后的结果。 
# 
#  如果在两个分区中，存在某个元素 nums[i] 被分在不同的组中，则认为这两个分区不同。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,4], k = 4
# 输出：6
# 解释：好分区的情况是 ([1,2,3], [4]), ([1,3], [2,4]), ([1,4], [2,3]), ([2,3], [1,4]), ([2
# ,4], [1,3]) 和 ([4], [1,2,3]) 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,3,3], k = 4
# 输出：0
# 解释：数组中不存在好分区。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [6,6], k = 2
# 输出：2
# 解释：可以将 nums[0] 放入第一个分区或第二个分区中。
# 好分区的情况是 ([6], [6]) 和 ([6], [6]) 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length, k <= 1000 
#  1 <= nums[i] <= 10⁹ 
#  
# 
#  Related Topics 数组 动态规划 👍 41 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countPartitions(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 反向思维 左边是坏分区的方案数 * 2 就是总的坏分区方案数  好方案数=2**n-2-坏方案数 需排除sum(nums)小于2k的情况
        # 求前i个数构造小于k的方案数
        # dp[i][j] 表示前i个数构造等于j的方案数
        # 不选择i则 dp[i][j] = dp[i-1][j]
        # 选择i则 dp[i][j] = dp[i-1][j-nums[i]]
        # 坏方案数 = dp[n][0] + ... + dp[n][k-1]
        if sum(nums) < 2 * k:
            return 0
        MOD = 10 ** 9 + 7
        dp = [[0] * k for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(0, k):
                dp[i][j] = (dp[i - 1][j] + (dp[i - 1][j - nums[i - 1]] if j - nums[i - 1] >= 0 else 0)) % MOD
        return (pow(2, len(nums), MOD) - sum(dp[-1]) * 2) % MOD

        # # 倒序循环 压缩空间
        # dp = [0] * k
        # dp[0] = 1
        # for i in range(1, len(nums) + 1):
        #     for j in range(k - 1, nums[i - 1] - 1, -1):
        #         dp[j] = (dp[j] + (dp[j - nums[i - 1]] if j - nums[i - 1] >= 0 else 0)) % MOD
        # return (pow(2, len(nums), MOD) - sum(dp) * 2) % MOD


    # 回溯
    #     self._rst = 0
    #     self.nums = nums
    #     self.k = k
    #
    #     self.backtrace(0, [], [])
    #     return self._rst
    #
    # def backtrace(self, idx, left, right):
    #     if idx == len(self.nums):
    #         if sum(left) >= self.k and sum(right) >= self.k:
    #             self._rst += 1
    #         return
    #     left.append(self.nums[idx])
    #     self.backtrace(idx + 1, left, right)
    #     left.pop()
    #     right.append(self.nums[idx])
    #     self.backtrace(idx + 1, left, right)
    #     right.pop()

# leetcode submit region end(Prohibit modification and deletion)
# if __name__ == '__main__':
#     print(Solution().countPartitions([1, 2, 3, 4], 4))
