

class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0, 1, 2, 3]

        for i in range(4, n + 1):
            # 最后一下按A
            dp[i] = dp[i - 1] + 1

            # 最后一下按Ctrl V
            # 从j开始重复复制
            for j in range(2, i + 1):
                dp[i] = max(dp[i], dp[j - 2] * (i - j + 1))
        return dp[n]
