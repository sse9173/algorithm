// 20210727
// LeetCode

import java.util.Arrays;

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        if(nums.length == 3) return (nums[0] + nums[1] + nums[2]);
        Arrays.sort(nums);
        int diff = 50000, ret = 0;
        for(int i = 0; i < nums.length; ++i){
            int s = i + 1, e = nums.length - 1;
            while(s < e){
                int sum = nums[i] + nums[s] + nums[e];
                if(sum == target) return sum;
                int tdiff = Math.abs(sum - target);
                if(tdiff < diff){
                    ret = sum; diff = tdiff;
                }
                if(sum < target) ++s;
                else --e;
            }
        }
        return ret;
    }
}
