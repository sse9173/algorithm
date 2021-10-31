# 20211028
# LeetCode

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        if len(nums) == 3 and sum(nums) == 0: return [nums,]
        ret = list()
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0: l += 1
                elif s > 0: r -= 1
                else:
                    ret.append([nums[i], nums[l], nums[r]])
                    while nums[l] == ret[-1][1] and l < r: l += 1
                    while nums[r] == ret[-1][2] and l < r: r -= 1
            i += 1
        return ret

