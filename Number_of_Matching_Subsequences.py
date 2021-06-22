# 20210622
# LeetCode

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ret, pool = 0, dict()
        for word in words:
            if word in pool:
                ret += pool[word]
                continue
            iterS = iter(s)
            res = all(c in iterS for c in word)
            pool[word] = 1 if res is True else 0
            ret += pool[word]
        return ret

