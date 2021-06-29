// 20210629
// LeetCode

class Solution {
    public int longestOnes(int[] nums, int k) {
        if(k == nums.length) return k;
        int ret = 0, len = 0, h = 0, t = 0;
        int[] q = new int[nums.length];
        for(int i = 0; i  < nums.length; ++i){
            if(nums[i] == 1) ++len;
            else if(k > 0){ --k; ++len; q[t++] = i; }
            else{
                if(ret < len) ret = len;
                q[t++] = i;
                len = i - q[h++];
            }
        }
        return ((ret >= len) ? ret : len);
    }
}
