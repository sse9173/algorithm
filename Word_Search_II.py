# 20211009
# LeetCode

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ret = list()
        m, n = len(board), len(board[0])
        trie = dict()

        for word in words:
            tr = trie
            for c in word:
                if c not in tr:
                    tr[c] = dict()
                tr = tr[c]
            tr['end'] = True

        def searchBoard(y, x, tr, tr_s):
            if 'end' in tr and tr_s not in ret: ret.append(tr_s)
            c = board[y][x]
            board[y][x] = '.'
            if y > 0 and board[y - 1][x] in tr: searchBoard(y - 1, x, tr[board[y - 1][x]], tr_s + board[y - 1][x])
            if x < n - 1 and board[y][x + 1] in tr: searchBoard(y, x + 1, tr[board[y][x + 1]], tr_s + board[y][x + 1])
            if y < m - 1 and board[y + 1][x] in tr: searchBoard(y + 1, x, tr[board[y + 1][x]], tr_s + board[y + 1][x])
            if x > 0 and board[y][x - 1] in tr: searchBoard(y, x - 1, tr[board[y][x - 1]], tr_s + board[y][x - 1])
            board[y][x] = c

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    searchBoard(i, j, trie[board[i][j]], board[i][j])

        return ret
