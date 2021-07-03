// 20210702
// LeetCode
// *** Not Optimized ***

class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Integer> ret = new ArrayList<>(k);
        if(k == arr.length){
            for(int num: arr) ret.add(num);
            return ret;
        }
        int i, j, idx;
        for(idx = 0; (idx < arr.length)&&(arr[idx] < x); ++idx);
        if((idx == arr.length)||(idx > 0)&&((x - arr[idx - 1]) <= (arr[idx] - x))) --idx;
        ret.add(arr[idx]); --k;
        i = idx - 1; j = idx + 1;
        while((k > 0)&&(i >= 0)&&(j < arr.length)){
            if((x - arr[i]) <= (arr[j] - x)) ret.add(0, arr[i--]);
            else ret.add(arr[j++]);
            --k;
        }
        for(; (k > 0)&&(i >= 0); --i, --k) ret.add(0, arr[i]);
        for(; (k > 0)&&(j < arr.length); ++j, --k) ret.add(arr[j]);
        return ret;
    }
}
