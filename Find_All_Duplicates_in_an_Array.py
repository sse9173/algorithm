# 20211006
# LeetCode

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = list()
        for i in range(len(nums)):
            num = abs(nums[i]) - 1
            if nums[num] < 0: ret.append(num + 1)
            else: nums[num] *= -1
        return ret

