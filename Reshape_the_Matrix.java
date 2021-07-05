// 20210705
// LeetCode

class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int m = mat.length, n = mat[0].length;
        if(m*n != r*c) return mat;
        int[][] rmat = new int[r][c];
        for(int k = 0, i = 0; i < m; ++i){
            for(int j = 0; j < n; ++j, ++k){
                rmat[k/c][k%c] = mat[i][j];
            }
        }
        return rmat;
    }
}
