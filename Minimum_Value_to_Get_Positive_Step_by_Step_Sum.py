# 20211111
# LeetCode

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minSum, tSum = 100, 0
        for num in nums:
            tSum += num
            minSum = min(minSum, tSum)
        return 1 if minSum > 0 else -minSum + 1
