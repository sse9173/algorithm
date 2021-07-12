// 20210712
// LeetCode

class Solution {
    public boolean isIsomorphic(String s, String t) {
        int[] smap = new int[128];
        int[] tmap = new int[128];
        for(int i = 0, sd = 0, td = 0; i < s.length(); ++i){
            int sc = s.charAt(i);
            if(smap[sc] == 0) smap[sc] = ++sd;
            int tc = t.charAt(i);
            if(tmap[tc] == 0) tmap[tc]  = ++td;
            if(smap[sc] != tmap[tc]) return false;
        }
        return true;
    }
}
