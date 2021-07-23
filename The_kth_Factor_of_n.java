// 20210723
// LeetCode

class Solution {
    public int kthFactor(int n, int k) {
        if(k == 1) return 1;
        int list[] = new int[n];
        list[0] = 1;
        int nfac = 1;
        for(int num = 2; num <= n; ++num){
            if(n%num != 0) continue;
            if(nfac + 1 == k) return num;
            if((num*num == n)||(list[nfac - 1]*num == n)) break;
            list[nfac++] = num;
        }
        k -= nfac;
        if(list[nfac - 1]*list[nfac - 1] == n){
            if(k >= nfac) return -1;
            return n/list[nfac - k];
        }
        else if(k > nfac) return -1;
        return n/list[nfac - k];
    }
}
