# 20210614
# LeetCode

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse = True, key = lambda x: x[1])
        if boxTypes[0][0] >= truckSize: return boxTypes[0][1]*truckSize
        ret = boxTypes[0][1]*boxTypes[0][0]
        truckSize -= boxTypes[0][0]
        for num, units in boxTypes[1:]:
            ret += units*min(num, truckSize)
            truckSize -= num
            if truckSize <= 0: break
        return ret
