# 20211212
# LeetCode

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot&1: return False
        subsum = tot>>1
        dp = [True,] + [False,]*subsum
        for num in nums:
            for i in range(subsum, num - 1, -1):
                dp[i] |= dp[i - num]
        return dp[subsum]

