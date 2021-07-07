// 20210707
// LeetCode

/* Not Optimized
 * (Optimized version seems to use binary search with bound)
 * Runtime: 17 ms
 * Memory Usage: 44.1 MB */
class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        List<Integer> line = new ArrayList<>(n*n);
        for(int i = 0; i < n; ++i) for(int num:matrix[i]) line.add(num);
        line.sort(null);
        return line.get(k - 1);
    }
}
