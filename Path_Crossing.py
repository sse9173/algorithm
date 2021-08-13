# 20210813
# LeetCode

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        v = [(0, 0), ]
        mv = {'N':[-1, 0], 'S':[1, 0], 'E': [0, 1], 'W':[0, -1]}
        r, c = 0, 0
        for d in path:
            r += mv[d][0]
            c += mv[d][1]
            if (r, c) in v: return True
            v.append((r, c))
        return False
