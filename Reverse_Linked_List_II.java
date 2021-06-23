// 20210623
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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(head.next == null) return head;
        ListNode ll = null, tr = head;
        int i;
        for(i = 1; i < left; ++i){
            ll = tr; tr = tr.next;
        }
        ListNode rev = new ListNode(tr.val, null);
        ListNode rr = rev;
        for(; i < right; ++i){
            tr = tr.next;
            ListNode n = new ListNode(tr.val, rev);
            rev = n;
        }
        if(ll != null) ll.next = rev;
        else head = rev;
        rr.next = tr.next;
        return head;
    }
}
