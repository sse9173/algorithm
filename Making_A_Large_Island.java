// 20210801
// LeetCode

/* NOT OPTIMIZED */

class Solution {
    public int[] id_area;
    public int maxid, n, gcnt;
    public int[][] v;

    public void dfs(int[][] grid, int r, int c){
        v[r][c] = maxid; ++gcnt;
        if((r > 0)&&(grid[r - 1][c] == 1)&&(v[r - 1][c] == 0)) dfs(grid, r - 1, c);
        if((c < n - 1)&&(grid[r][c + 1] == 1)&&(v[r][c + 1] == 0)) dfs(grid, r, c + 1);
        if((r < n - 1)&&(grid[r + 1][c] == 1)&&(v[r + 1][c] == 0)) dfs(grid, r + 1, c);
        if((c > 0)&&(grid[r][c - 1] == 1)&&(v[r][c - 1] == 0)) dfs(grid, r, c - 1);
    }

    public int largestIsland(int[][] grid) {
        n = grid.length;
        if(n == 1) return 1;
        id_area = new int[n*n + 1];
        maxid = 1;
        v = new int[n][n];
        int[][] zeroes = new int[n*n][2];
        int maxz = 0, ret = 0;
        for(int i = 0; i < n; ++i) for(int j = 0; j < n; ++j){
            if(grid[i][j] == 0){
                zeroes[maxz][0] = i; zeroes[maxz][1] = j;
                ++maxz;
            }
            else if(v[i][j] == 0){
                gcnt = 0;
                dfs(grid, i, j);
                id_area[maxid++] = gcnt;
                if(ret < gcnt) ret = gcnt;
            }
        }
        if(maxz == 0) return ret;
        for(int i = 0; i < maxz; ++i){
            int r = zeroes[i][0], c = zeroes[i][1], area = 1;
            int[] ids = new int[maxid + 1];
            if(r > 0){
                area += id_area[v[r - 1][c]];
                ids[v[r - 1][c]] = 1;
            }
            if((c < n - 1)&&(ids[v[r][c + 1]] == 0)){
                area += id_area[v[r][c + 1]];
                ids[v[r][c + 1]] = 1;
            }
            if((r < n - 1)&&(ids[v[r + 1][c]] == 0)){
                area += id_area[v[r + 1][c]];
                ids[v[r + 1][c]] = 1;
            }
            if((c > 0)&&(ids[v[r][c - 1]] == 0)){
                area += id_area[v[r][c - 1]];
            }
            if(ret < area) ret = area;
        }
        return ret;
    }
}
