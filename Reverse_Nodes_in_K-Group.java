// 20210718
// LeetCode

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if(k == 1) return head;
        int sz = 0;
        for(ListNode tr = head; tr != null; ++sz) tr = tr.next;
        sz -= (sz%k);
        ListNode retp = new ListNode();
        ListNode plast = retp;
        for(int i = 0; i < sz; i += k){
            ListNode last = head, start = null;
            for(int j = 0; j < k; ++j){
                ListNode tmp = head;
                head = head.next;
                tmp.next = start;
                start = tmp;
            }
            plast.next = start;
            last.next = head;
            plast = last;
        }
        return retp.next;
    }
}
