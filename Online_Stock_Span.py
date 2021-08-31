# 20210831
# LeetCode

class StockSpanner:

    def __init__(self):
        self.prices = list()
        self.vals = list()

    def next(self, price: int) -> int:
        val = 1
        while len(self.prices) > 0 and self.prices[-1] <= price:
            val += self.vals[-1]
            self.prices.pop()
            self.vals.pop()
        self.prices.append(price)
        self.vals.append(val)
        return val


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
