// 20210729
// LeetCode

class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        int[][] ret = new int[m][n];
        int far = m + n - 2;
        for(int i = 0; i < m; ++i) for(int j = 0; j < n; ++j){
            if(mat[i][j] == 0) continue;
            int up = ((i > 0) ? ret[i - 1][j] : far);
            int left = ((j > 0) ? ret[i][j - 1] : far);
            ret[i][j] = Math.min(up, left) + 1;
        }
        for(int i = m - 1; i >= 0; --i) for(int j = n - 1; j >= 0; --j){
            if(mat[i][j] == 0) continue;
            int down = ((i < m - 1) ? ret[i + 1][j] : far);
            int right = ((j < n - 1) ? ret[i][j + 1] : far);
            ret[i][j] = Math.min(ret[i][j], Math.min(down, right) + 1);
        }
        return ret;
    }
}
