# 20211008
# LeetCode

class Trie:

    def __init__(self):
        self.head = dict()

    def insert(self, word: str) -> None:
        cur = self.head
        i = 0
        while i < len(word) and word[i] in cur:
            cur = cur[word[i]]
            i += 1
        if i == len(word): cur['end'] = True
        else:
            for c in word[i:]:
                cur[c] = dict()
                cur = cur[c]
                cur['end'] = False
            cur['end'] = True

    def search(self, word: str) -> bool:
        cur = self.head
        for c in word:
            if c not in cur: return False
            cur = cur[c]
        return cur['end']

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for c in prefix:
            if c not in cur: return False
            cur = cur[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
