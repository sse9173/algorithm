# 20211223
# LeetCode

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = defaultdict(list)
        for a, b in prerequisites: pre[a].append(b)
        ret, v = list(), set()

        def dfs(course):
            nonlocal pre, ret, v
            if course in ret: return True
            if course in v: return False
            v.add(course)
            if course in pre:
                for p in pre[course]:
                    if not dfs(p): return False
            ret.append(course)
            return True

        for course in range(numCourses):
            if course not in ret:
                if not dfs(course): return []

        return ret

