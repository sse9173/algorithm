# 20211027
# LeetCode

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0, 0, 0]
        for num in nums: cnt[num] += 1
        i = 0
        for j in range(cnt[0]):
            nums[i] = 0
            i += 1
        for j in range(cnt[1]):
            nums[i] = 1
            i += 1
        for j in range(cnt[2]):
            nums[i] = 2
            i += 1

