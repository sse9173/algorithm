// 20210719
// LeetCode

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(p.val > q.val){
            TreeNode tmp = p;
            p = q;
            q = tmp;
        }
        while(root != null){
            if((p.val <= root.val)&&(root.val <= q.val)) break;
            if(root.val < p.val) root = root.right;
            else root = root.left;
        }
        return root;
    }
}
