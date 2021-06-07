# 20210607
# LeetCode

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        tc0, tc1 = cost[0:2]
        for c in cost[2:]:
            tc = c + min(tc0, tc1)
            tc0, tc1 = tc1, tc
        return min(tc0, tc1)
