# 20211003
# LeetCode

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        dist = 1
        for num in nums[-2::-1]:
            if num < dist: dist += 1
            else: dist = 1
        return (dist == 1)

