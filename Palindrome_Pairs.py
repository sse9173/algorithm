# 20210613
# LeetCode

class Solution:
    def  __init__(self):
        self.trie = {'tree':dict(), 'idx':set()}

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        self.trie['idx'] = [i for i in range(len(words))]
        nullStr, palStr = -1, list()
        for i in range(len(words)):
            if words[i] == "": nullStr = i
            elif words[i] == words[i][::-1]: palStr.append(i)
            tr = self.trie['tree']
            for c in words[i]:
                if c not in tr: tr[c] = {'tree':dict(), 'idx':set()}
                tr[c]['idx'].add(i)
                tr = tr[c]['tree']
        ret = list()
        if nullStr != -1:
            for idx in palStr: ret += [[nullStr, idx], [idx, nullStr]]
        for i in range(len(words)):
            tr = self.trie
            v = set()
            v.add(i)
            for c in words[i][::-1]:
                if c not in tr['tree']: break
                tr = tr['tree'][c]
                idxs = list(tr['idx'] - v)
                if len(v) == 0: break
                for idx in idxs:
                    cand = words[idx] + words[i]
                    if cand == cand[::-1]: ret.append([idx, i])
                    v.add(idx)
        return ret

