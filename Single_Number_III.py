# 20211106
# LeetCode

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ret = set()
        for num in nums:
            if num in ret: ret.remove(num)
            else: ret.add(num)
        return list(ret)
