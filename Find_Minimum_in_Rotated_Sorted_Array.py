# 20210831
# LeetCode

class Solution:
    def findMin(self, nums: List[int]) -> int:
        s, e = 0, len(nums) - 1
        while nums[s] > nums[e]:
            m = (s + e)>>1
            if m == s: return nums[e]
            if nums[m] < nums[e]: e = m
            else: s = m
        return nums[s]

