// 20210706
// LeetCode

/* Optimized Version
 * Runtime: 23 ms
 * Memory: 51.6 MB */
import java.util.Arrays;
class Solution {
    public int minSetSize(int[] arr) {
        int[] vcnt = new int[100001];
        for(int num:arr) ++vcnt[num];
        Arrays.sort(vcnt);
        int d = 100000;
        for(int l = arr.length, tr = 0; tr < (l>>1); --d) tr += vcnt[d];
        return 100000 - d;
    }
}

/* Segment Tree <- very bad case
 * Runtime: 448 ms
 * Memory: 69.8 MB
class Solution {
    int[][] tree = new int[400001][2];
    public void update(int node, int s, int e, int idx, int val){
        if((idx < s)||(e < idx)) return;
        if(s == e){
            if(tree[node][1] == 0) tree[node][1] = idx;
            if(val == 1) ++tree[node][0];
            else tree[node][0] = 0;
            return;
        }
        int m = (s + e)>>1;
        update(node<<1, s, m, idx, val);
        update((node<<1) + 1, m + 1, e, idx, val);
        int lval = tree[(node<<1)][0], lidx = tree[(node<<1)][1];
        int rval = tree[(node<<1) + 1][0], ridx = tree[(node<<1) + 1][1];
        if(lval >= rval){
            tree[node][0] = lval; tree[node][1] = lidx;
        } else{
            tree[node][0] = rval; tree[node][1] = ridx;
        }
    }
    public int minSetSize(int[] arr) {
        int l = arr.length, sub = 0, ret = 0;
        for(int num:arr) update(1, 1, 100000, num, 1);
        while(sub < (l>>1)){
            ++ret;
            sub += tree[1][0];
            update(1, 1, 100000, tree[1][1], 0);
        }
        return ret;
    }
}
*/
