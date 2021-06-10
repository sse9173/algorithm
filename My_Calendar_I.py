# 20210610
# LeetCode

class MyCalendar:
    def __init__(self):
        self.reserved = {'s': -1, 'e': -1, 'n': {'s': 1000000005, 'e': 1000000005}}

    def book(self, start: int, end: int) -> bool:
        rsv = self.reserved
        while start > rsv['s']:
            prev, rsv = rsv, rsv['n']
        if start < prev['e'] or end > rsv['s']: return False
        prev['n'] = {'s': start, 'e': end, 'n': rsv}
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
