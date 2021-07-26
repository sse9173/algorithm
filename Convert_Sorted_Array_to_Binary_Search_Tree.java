// 20210726
// LeetCode

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode recurse(int s, int e, int[] nums){
        if(s > e) return null;
        if(s == e) return new TreeNode(nums[s], null, null);
        int m = (s + e)>>1;
        return new TreeNode(nums[m], recurse(s, m - 1, nums), recurse(m + 1, e, nums));
    }
    public TreeNode sortedArrayToBST(int[] nums) {
        return recurse(0, nums.length - 1, nums);
    }
}
