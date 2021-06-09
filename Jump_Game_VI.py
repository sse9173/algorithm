# 20210609
# LeetCode

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        q = [0, ]
        for i in range(1, len(nums)):
            if q[0] < i - k: q.pop(0)
            nums[i] += nums[q[0]]
            while len(q) != 0 and nums[q[-1]] <= nums[i]: q.pop()
            q.append(i)
        return nums[-1]

