# 20210928
# LeetCode

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        chg = [list(), list()]
        for i in range(len(nums)):
            if i&1 != nums[i]&1:
                if len(chg[i&1]) != 0:
                    idx = chg[i&1].pop()
                    nums[i], nums[idx] = nums[idx], nums[i]
                else: chg[~(i&1)].append(i)
        return nums

