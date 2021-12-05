# 20211204
# LeetCode

class StreamChecker:
    def __init__(self, words: List[str]):
        self.db = dict()
        for word in words:
            node = self.db
            for c in word[::-1]:
                if c not in node: node[c] = dict()
                node = node[c]
            node['$'] = True
        self.stream = ""

    def query(self, letter: str) -> bool:
        self.stream += letter
        node = self.db
        for c in self.stream[::-1]:
            if '$' in node: return True
            if c not in node: return False
            node = node[c]
        return True if '$' in node else False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
