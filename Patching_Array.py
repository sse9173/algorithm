# 20210829
# LeetCode

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patched, idx, complete = 0, 0, 1
        while complete <= n:
            if idx < len(nums) and complete >= nums[idx]:
                complete += nums[idx]
                idx += 1
            else:
                patched += 1
                complete += complete
        return patched
