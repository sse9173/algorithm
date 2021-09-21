# 20210921
# LeetCode

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret, cur = 0, 0
        for num in nums:
            if num == 1: cur += 1
            else:
                if ret < cur: ret = cur
                cur = 0
        return max(ret, cur)

