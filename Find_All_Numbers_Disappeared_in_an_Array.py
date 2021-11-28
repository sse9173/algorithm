# 20211118
# LeetCode

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret = set([i for i in range(1, len(nums) + 1)])
        for num in nums: ret.discard(num)
        return list(ret)

