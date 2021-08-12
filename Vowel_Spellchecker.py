# 20210812
# LeetCode

# not optimized (very slow)
import re
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        ret = list()
        capset = dict() # capitalization
        vset = dict()   # vowel errors
        for word in wordlist:
            key = word.lower()
            if key in capset: capset[key].append(word)
            else: capset[key] = [word,]
            for vowel in ['a', 'e', 'i', 'o', 'u']: key = key.replace(vowel, '.')
            if key in vset: vset[key].append(word)
            else: vset[key] = [word, ]
        for word in queries:
            lword, vword = word.lower(), word.lower()
            for vowel in ['a', 'e', 'i', 'o', 'u']: vword = vword.replace(vowel, '.')
            if lword in capset:
                if word in capset[lword]: ret.append(word)
                else: ret.append(capset[lword][0])
            elif vword in vset: ret.append(vset[vword][0])
            else: ret.append("")
        return ret

