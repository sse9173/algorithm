# 20211125
# LeetCode

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret, cur = nums[0], nums[0]
        for num in nums[1:]:
            cur = max(cur + num, num)
            ret = max(ret, cur)
        return ret
