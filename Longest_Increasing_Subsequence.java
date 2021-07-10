// 20210709
// LeetCode

/* Binary Search with Lower Bound 
 * (also can solve by segment tree) */
class Solution {
    public int lengthOfLIS(int[] nums) {
        int l = nums.length, last = 0;
        int[] L = new int[l];
        L[0] = nums[0];
        for(int i = 1; i < l; ++i){
            if(nums[i] > L[last]) L[++last] = nums[i];
            else{
                int s = 0, e = last;
                while(s < e){
                    int m = (s + e)>>1;
                    if(nums[i] <= L[m]) e = m;
                    else s = m + 1;
                }
                L[s] = nums[i];
            }
        }
        return last + 1;
    }
}
