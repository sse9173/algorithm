# 20211109
# LeetCode

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        wpool = dict()
        for word in words:
            key = 0
            for c in word: key |= 1<<(ord(c) - ord('a'))
            if key not in wpool: wpool[key] = 1
            else: wpool[key] += 1
        ret = list()
        for puzzle in puzzles:
            key, first = 0, 1<<(ord(puzzle[0]) - ord('a'))
            for c in puzzle[1:]: key |= 1<<(ord(c) - ord('a'))
            tkey, cnt = key, 0 if first not in wpool else wpool[first]
            while tkey:
                if tkey|first in wpool: cnt += wpool[tkey|first]
                tkey = (tkey - 1)&key
            ret.append(cnt)
        return ret

