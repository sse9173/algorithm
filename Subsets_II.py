# 20210803
# LeetCode

class Solution:
    ret = list()
    def recurse(self, nums, idx, elem):
        if idx == len(nums): return
        for i in range(idx, len(nums)):
            if elem + [nums[i], ] in self.ret: continue
            self.ret.append(elem + [nums[i], ])
            self.recurse(nums, i + 1, elem + [nums[i], ])

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ret = [[], ]
        nums.sort()
        self.recurse(nums, 0, [])
        return self.ret

