# 20210830
# LeetCode

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        numsL, globalV = len(nums), set()
        for start in range(len(nums)):
            if len(globalV) == numsL: break
            if start in globalV: continue
            pos, prev, localV = start, 0, [start, ]
            while True:
                pos = (pos + nums[pos])%len(nums)
                if prev*nums[pos] < 0: break
                prev = nums[pos]
                if pos in localV:
                    if len(localV) != localV.index(pos) + 1: return True
                    else: break
                localV.append(pos)
            globalV |= set(localV)
        return False

