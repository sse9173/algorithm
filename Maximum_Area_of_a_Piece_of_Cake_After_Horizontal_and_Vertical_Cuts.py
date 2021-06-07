# 20210604
# LeetCode

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        maxh = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            maxh = max(maxh, horizontalCuts[i] - horizontalCuts[i - 1])
        verticalCuts.sort()
        maxv = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            maxv = max(maxv, verticalCuts[i] - verticalCuts[i - 1])
        return (maxh*maxv)%1000000007
