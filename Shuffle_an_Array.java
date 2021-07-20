// 20210720
// LeetCode

import java.util.Random;

class Solution {
    int[] orig;
    int len;
    Random random = new Random();

    public Solution(int[] nums) {
        orig = nums;
        len = nums.length;
    }

    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return orig;
    }

    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        if(len == 1) return orig;
        int[] rand = orig.clone();
        for(int i = len - 1; i >= 0; --i){
            int j = random.nextInt(i + 1);
            int tmp = rand[i];
            rand[i] = rand[j];
            rand[j] = tmp;
        }
        return rand;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */
