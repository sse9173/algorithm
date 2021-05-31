# 20210527
# LeetCode

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ret = list()
        for i in range(len(searchWord)):
            r = list()
            delList = list()
            for p in products:
                if p[:i + 1] == searchWord[:i + 1]:
                    r.append(p)
                    if len(r) == 3: break
                else: delList.append(p)
            for delitem in delList: products.remove(delitem)
            ret.append(r)
        return ret
