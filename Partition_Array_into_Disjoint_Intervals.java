// 20210722
// LeetCode

class Solution {
    public int partitionDisjoint(int[] nums) {
        int idx = 0, cmp = nums[0], locmax = nums[0];
        for(int i = 1; i < nums.length; ++i){
            if(nums[i] < cmp){
                idx = i;
                cmp = locmax;
            }
            else if(locmax < nums[i]) locmax = nums[i];
        }
        return idx + 1;
    }
}
