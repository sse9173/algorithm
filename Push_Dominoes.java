// 20210721
// LeetCode

class Solution {
    public String pushDominoes(String dominoes) {
        char[] dom = dominoes.toCharArray();
        int n = dom.length, lastL = 0, lastR = 0, dir = 0;
        for(int i = 0; i < n; ++i){
            if(dom[i] == 'L'){
                if(dir == 0) for(int j = i - 1; j >= lastL; --j) dom[j] = 'L';
                else{
                    for(int j = ((lastR + i)>>1) + 1; j < i; ++j) dom[j] = 'L';
                    if(((lastR + i)&1) == 0) dom[(lastR + i)>>1] = '.';
                    dir = 0;
                }
                lastL = i;
            }
            else if(dom[i] == 'R'){
                lastR = i;
                dir = 1;
            }
            else if(dir == 1) dom[i] = 'R';
        }
        return new String(dom);
    }
}
