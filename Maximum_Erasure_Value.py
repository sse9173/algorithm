# 20210529
# LeetCode

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        head = 0
        tail = 1
        elem = set()
        elem.add(nums[0])
        maxScore = 0
        score = nums[0]
        for tail in range(1, len(nums)):
            num = nums[tail]
            if num in elem:
                while nums[head] != num:
                    elem.remove(nums[head])
                    score -= nums[head]
                    head += 1
                head += 1
            else:
                elem.add(num)
                score += num
                if maxScore < score: maxScore = score
        return maxScore
