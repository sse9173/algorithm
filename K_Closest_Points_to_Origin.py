# 20211226
# LeetCode

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = defaultdict(list)
        for y, x in points: dist[y*y + x*x].append([y, x])
        dist = sorted(dist.items())
        ret = list()
        for d in dist:
            ret += d[1]
            if len(ret) >= k: break
        return ret

