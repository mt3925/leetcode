# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] r
# epresents the width and the height of an envelope. 
# 
#  One envelope can fit into another if and only if both the width and height of
#  one envelope are greater than the other envelope's width and height. 
# 
#  Return the maximum number of envelopes you can Russian doll (i.e., put one in
# side the other). 
# 
#  Note: You cannot rotate an envelope. 
# 
#  
#  Example 1: 
# 
#  
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] 
# => [5,4] => [6,7]).
#  
# 
#  Example 2: 
# 
#  
# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= envelopes.length <= 5000 
#  envelopes[i].length == 2 
#  1 <= wi, hi <= 104 
#  
#  Related Topics 二分查找 动态规划 
#  👍 499 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         env_cnt = len(envelopes)
#         envelopes.sort()
#
#         cnt_map = {}
#         def dp(cur_idx):
#             if cur_idx in cnt_map:
#                 return cnt_map[cur_idx]
#             max_cnt = 1
#             for idx in range(cur_idx + 1, env_cnt):
#                 if envelopes[idx][0] > envelopes[cur_idx][0] and envelopes[idx][1] > envelopes[cur_idx][1]:
#                     cnt = dp(idx) + 1
#                     max_cnt = max(cnt, max_cnt)
#             cnt_map[cur_idx] = max_cnt
#             return max_cnt
#         return max([dp(i) for i in range(env_cnt)])


# class Solution:
#     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         env_cnt = len(envelopes)
#         envelopes.sort(key=lambda x: (x[0],  -x[1]))
#
#         dp = [1] * env_cnt
#         for i in range(1, env_cnt):
#             cnt = 1
#             for j in range(0, i):
#                 if envelopes[j][1] < envelopes[i][1]:
#                     cnt = max(cnt, dp[j] + 1)
#             dp[i] = cnt
#         return max(dp)


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        top_list = []

        def find_first_bigger_top(top):
            if not top_list:
                return None
            left = 0
            right = len(top_list)
            while left < right:
                mid = (left + right) // 2
                if top_list[mid] >= top:
                    right = mid
                else:
                    left = mid + 1
            return left if left < len(top_list) else None

        for env in envelopes:
            pos = find_first_bigger_top(env[1])
            if pos is None:
                top_list.append(env[1])
            else:
                top_list[pos] = env[1]
        return len(top_list)


# leetcode submit region end(Prohibit modification and deletion)
# if __name__ == '__main__':
#     print(Solution().maxEnvelopes([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]))
#     print(Solution().maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
