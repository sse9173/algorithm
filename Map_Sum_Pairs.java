// 20210730
// LeetCode

class Node{
    public int val;
    public Node next[];

    public Node(){
        this.val = 0;
        this.next = new Node[26];
    }
}
class MapSum {
    public Node root;

    /** Initialize your data structure here. */
    public MapSum() {
        root = new Node();
    }

    public void Rinsert(Node trace, String key, int idx, int val){
        if(key.length() == idx){
            trace.val = val;
            return;
        }
        int c = (int)(key.charAt(idx) - 'a');
        if(trace.next[c] == null) trace.next[c] = new Node();
        Rinsert(trace.next[c], key, idx + 1, val);
    }

    public void insert(String key, int val) {
        Rinsert(root, key, 0, val);
    }

    public int Rsum(Node trace){
        if(trace == null) return 0;
        int valsum = trace.val;
        for(int i = 0; i < 26; ++i) valsum += Rsum(trace.next[i]);
        return valsum;
    }

    public int sum(String prefix) {
        Node trace = root;
        for(int i = 0; i < prefix.length(); ++i){
            int c = (int)(prefix.charAt(i) - 'a');
            if(trace.next[c] == null) return 0;
            trace = trace.next[c];
        }
        return Rsum(trace);
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */
