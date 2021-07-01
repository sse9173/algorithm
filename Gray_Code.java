// 20210701
// LeetCode

import java.util.ArrayList;

class Solution {
    public List<Integer> grayCode(int n) {
        int limit = (1<<n) - 1;
        List<Integer> ret = new ArrayList<>(limit + 1);
        for(int i = 0; i <= limit; ++i) ret.add(i^(i>>1));
        return ret;
    }
}
