# 20211216
# LeetCode

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0,]
        if n == 2: return [0, 1]
        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        q = list()
        for node in g:
            if len(g[node]) == 1: q.append(node)
        while n > 2:
            n -= len(q)
            nq = list()
            for node in q:
                for adj in g[node]:
                    g[adj].remove(node)
                    if len(g[adj]) == 1: nq.append(adj)
            q = nq[:]
        return q
