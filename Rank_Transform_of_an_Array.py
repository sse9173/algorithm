# 20210813
# LeetCode

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0: return []
        sarr = sorted(set(arr))
        mapping = dict()
        for i in range(len(sarr)): mapping[sarr[i]] = i + 1
        return [mapping[num] for num in arr]
