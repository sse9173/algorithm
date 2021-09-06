# 20210906
# LeetCode

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ret, maxd = keysPressed[0], releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            time = releaseTimes[i] - releaseTimes[i - 1]
            if time > maxd: ret, maxd = keysPressed[i], time
            elif time == maxd and ret < keysPressed[i]: ret = keysPressed[i]
        return ret

