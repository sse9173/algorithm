# 20211020
# LeetCode

class Solution:
    def reverseWords(self, s: str) -> str:
        splitted = s.split(' ')
        ret = ""
        for word in splitted[::-1]:
            if word != '': ret += (word + ' ')
        return ret[:-1]
