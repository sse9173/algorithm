# 20211203
# LeetCode

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dpmin, dpmax = nums[:], nums[:]
        ret = nums[0]
        for i in range(1, len(nums)):
            t1, t2 = dpmin[i - 1]*nums[i], dpmax[i - 1]*nums[i]
            dpmin[i] = min(dpmin[i], t1, t2)
            dpmax[i] = max(dpmax[i], t1, t2)
            if ret < dpmax[i]: ret = dpmax[i]
        return ret

