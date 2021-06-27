// 20210627
// LeetCode

class Solution {
    public int candy(int[] ratings) {
        if(ratings.length == 1) return 1;
        int n = ratings.length;
        int [] candies = new int[n];
        candies[0] = candies[n - 1] = 1;
        for(int i = 1; i < n; ++i){
            if(ratings[i] > ratings[i - 1]) candies[i] = candies[i - 1] + 1;
            else candies[i] = 1;
        }
        for(int i = n - 2; i>= 0; --i){
            if((ratings[i] > ratings[i + 1])&&(candies[i] < candies[i + 1] + 1))
                candies[i] = candies[i + 1] + 1;
        }
        int tot = candies[0];
        for(int i = 1; i < n; ++i) tot += candies[i];
        return tot;
    }
}
