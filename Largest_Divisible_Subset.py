# 20211115
# LeetCode

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cand = [[nums[i],] for i in range(len(nums))]
        ret = cand[0]
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i]%nums[j] == 0 and len(cand[i]) <= len(cand[j]):
                    cand[i] = cand[j] + [nums[i],]
                    if len(ret) < len(cand[i]): ret = cand[i]
        return ret

