// 20210713
// LeetCode

class Solution {
    public int findPeakElement(int[] nums) {
        if(nums.length == 1) return 0;
        int s = 0, e = nums.length - 1;
        while(s <= e){
            int m = (s + e)>>1;
            if(m == 0) return ((nums[0] > nums[1]) ? 0 : 1);
            if(m == nums.length - 1) return ((nums[m - 1] > nums[m]) ? m - 1 : m);
            if((nums[m - 1] < nums[m])&&(nums[m] > nums[m + 1])) return m;
            if(nums[m - 1] > nums[m]) e = m - 1;
            else s = m + 1;
        }
        return -1;
    }
}
