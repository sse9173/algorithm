# 20211129
# LeetCode

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        db = dict()
        for account in accounts:
            name, addr = account[0], set(account[1:])
            if name not in db: db[name] = [addr,]
            else:
                for elem in db[name]:
                    if len(addr&elem) > 0:
                        addr |= elem
                        elem.clear()
                db[name].append(addr)
        ret = list()
        for name, addrs in db.items():
            for addr in addrs:
                if len(addr) > 0: ret.append([name,] + list(sorted(addr)))
        return ret
