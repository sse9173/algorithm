# 20210927
# LeetCode

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        pool = set()
        for email in emails:
            loc, dom = email.split('@')
            if '+' in loc: loc = loc[:loc.index('+')].replace('.', '')
            else: loc = loc.replace('.', '')
            pool.add(loc + '@' + dom)
        return len(pool)

