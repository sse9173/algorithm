# 20210901
# LeetCode

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        maxk, ret = len(nums), 0
        v = list(0 for _ in range(maxk))
        for i in range(maxk):
            j, counter = i, 0
            while v[j] == 0:
                v[j] = 1
                counter += 1
                j = nums[j]
            ret = max(ret, counter)
        return ret
