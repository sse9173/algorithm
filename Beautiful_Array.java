// 20210728
// LeetCode

class Solution {
    public int[] beautifulArray(int n) {
        int[] ret = new int[n];
        if(n == 1) return new int[] {1};
        else if(n == 2) return new int[] {1, 2};
        else{
            int[] odd = beautifulArray((n + 1)>>1);
            int[] even = beautifulArray(n>>1);
            for(int i = 0; i < odd.length; ++i) ret[i] = (odd[i]<<1) - 1;
            for(int i = 0; i < even.length; ++i) ret[i + odd.length] = even[i]<<1;
        }
        return ret;
    }
}
