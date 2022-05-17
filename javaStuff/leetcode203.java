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
    public ListNode removeElements(ListNode head, int val) {
        if(head==null)return head;
        while(head.val == val){
            if(head.next==null)return null;
            head = head.next;
        }
        ListNode nodePointer = head;
        while(nodePointer.next != null){
            if(nodePointer.next.val == val){
                nodePointer.next = nodePointer.next.next;
            }
            else{
                nodePointer = nodePointer.next;
            }
        }
        return head;
    }
}