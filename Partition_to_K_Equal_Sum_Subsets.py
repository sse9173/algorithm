# 20210930
# LeetCode

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 1: return True
        tot = sum(nums)
        if tot%k != 0: return False
        tg, v = tot//k, set()

        def recurse(val, idx, leftk):
            if leftk == 1: return True
            if val > tg: return False
            elif val == tg and leftk > 0: return recurse(0, 0, leftk - 1)
            for i in range(idx, len(nums)):
                if i not in v:
                    v.add(i)
                    if recurse(val + nums[i], i + 1, leftk) is True: return True
                    v.remove(i)
            return False

        return recurse(0, 0, k)
