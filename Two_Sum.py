# 20210802
# LeetCode

# Not Optimized
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nset = set(nums)
        v = set()
        for i in range(len(nums)):
            if nums[i] in v: continue
            if target - nums[i] in nset and target != 2*nums[i]:
                return [i, nums.index(target - nums[i])]
            elif target == 2*nums[i] and nums.count(nums[i]) > 1:
                return [i, i + 1 + nums[i + 1:].index(nums[i])]
            else: v.add(nums[i])

