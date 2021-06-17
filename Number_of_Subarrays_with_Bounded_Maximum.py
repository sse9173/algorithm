# 20210617
# LeetCode

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ret, avail, small = 0, 0, 0
        for num in nums:
            if num > right: avail = 0
            else:
                avail += 1
                ret += avail
            if num < left:
                small += 1
                ret -= small
            else: small = 0
        return ret

