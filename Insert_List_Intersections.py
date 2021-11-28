# 20211124
# LeetCode

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ret = list()
        fidx, sidx = 0, 0
        while fidx < len(firstList) and sidx < len(secondList):
            if firstList[fidx][0] <= secondList[sidx][1] and firstList[fidx][1] >= secondList[sidx][0]:
                ret.append([max(firstList[fidx][0], secondList[sidx][0]), min(firstList[fidx][1], secondList[sidx][1])])
            if firstList[fidx][1] < secondList[sidx][1]: fidx += 1
            else: sidx += 1
        return ret

