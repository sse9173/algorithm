# 20210812
# LeetCode

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs, ]
        wordset = dict()
        for word in strs:
            tword = "".join(sorted(word))
            if tword not in wordset: wordset[tword] = list()
            wordset[tword].append(word)
        return list(wordset.values())

