# 20211201
# LeetCode

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        a, b = nums[0], max(nums[0], nums[1])
        for num in nums[2:]:
            a, b = b, max(a + num, b)
        return b

