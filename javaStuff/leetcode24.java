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
    public ListNode swapPairs(ListNode head) {
        if(head == null || head.next == null) return head;
        ListNode leftNode = head;
        ListNode rightNode = head.next;
        ListNode newHead = rightNode;
        while(leftNode != null && rightNode != null){
            if(rightNode.next == null){
                leftNode.next = null;
                rightNode.next = leftNode;
                return newHead;
            }
            ListNode holder = rightNode.next;
            if(holder.next == null) leftNode.next = holder;
            else leftNode.next = holder.next;
            rightNode.next = leftNode;
            leftNode = holder;
            rightNode = holder.next;
        }
        return newHead;
    }
}