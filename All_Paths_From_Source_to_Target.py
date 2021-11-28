# 20211128
# LeetCode

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        tg = len(graph) - 1

        def recurse(path):
            nonlocal tg
            last = path[-1]
            if last == tg:
                ret.append(path[:])
                return
            if len(path) > tg: return
            for node in graph[last]:
                recurse(path + [node,])

        ret = list()
        recurse([0,])
        return ret
