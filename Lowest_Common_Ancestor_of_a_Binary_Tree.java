// 20210630
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
    TreeNode ret;
    public int recurse(TreeNode cur, int p, int q){
        if(cur == null) return 0;
        int e = (((cur.val == p)||(cur.val == q)) ? 1 : 0);
        e += (recurse(cur.left, p, q) + recurse(cur.right, p, q));
        if((e == 2)&&(ret == null)) ret = cur;
        return e;
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        ret = null;
        recurse(root, p.val, q.val);
        return ret;
    }
}
