# 20211126
# LeetCode

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]: return 0
        if target > nums[-1]: return len(nums)
        s, e = 0, len(nums) - 1
        while s < e:
            m = (s + e)>>1
            if nums[m] == target: return m
            elif nums[m] > target: e = m - 1
            else: s = m + 1
        return s + int(nums[s] < target)
