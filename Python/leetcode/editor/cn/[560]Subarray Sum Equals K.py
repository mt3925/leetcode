# Given an array of integers nums and an integer k, return the total number of c
# ontinuous subarrays whose sum equals to k. 
# 
#  
#  Example 1: 
#  Input: nums = [1,1,1], k = 2
# Output: 2
#  Example 2: 
#  Input: nums = [1,2,3], k = 3
# Output: 2
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2 * 104 
#  -1000 <= nums[i] <= 1000 
#  -107 <= k <= 107 
#  
#  Related Topics 数组 哈希表 前缀和 
#  👍 1012 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        sum_list = [0]
        for i in nums:
            sum_list.append(sum_list[-1] + i)

        sum_map = collections.defaultdict(int)
        rst = 0
        for i in sum_list:
            rst += sum_map.get(i - k, 0)
            sum_map[i] += 1
        return rst

# leetcode submit region end(Prohibit modification and deletion)
