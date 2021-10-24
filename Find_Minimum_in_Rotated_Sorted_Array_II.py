# 20211023
# LeetCode

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]: return nums[0]
        s, e = 0, len(nums) - 1
        while s < e:
            m = (s + e)>>1
            if nums[m] > nums[e]: s = m + 1
            elif nums[m] < nums[e]: e = m
            else: e -= 1
        return nums[e]
