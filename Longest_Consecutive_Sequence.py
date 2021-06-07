# 20210606
# LeetCode

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnum = set(nums)
        ret = 0
        for num in nums:
            if num + 1 in setnum: continue
            s = num
            length = 0
            while s in setnum:
                s -= 1
                length += 1
            ret = max(ret, length)
        return ret
