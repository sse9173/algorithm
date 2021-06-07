# 20210606
# LeetCode

import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = sorted(zip(efficiency, speed), reverse = True)
        maxPerf = 0
        spdHeap = list()
        perf = 0
        for eff, spd in eng:
            heapq.heappush(spdHeap, spd)
            if len(spdHeap) <= k: perf += spd
            else: perf += (spd - heapq.heappop(spdHeap))
            maxPerf = max(maxPerf, perf*eff)
        return maxPerf%1000000007
