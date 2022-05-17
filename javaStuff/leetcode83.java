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
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null) return head;
        ListNode nextPointer = head.next;
        ListNode currPointer = head;
        while(currPointer.next != null){
            if(nextPointer != null && nextPointer.val == currPointer.val){
                nextPointer = nextPointer.next;
            }
            else if(nextPointer != null){
                currPointer.next = nextPointer;
                currPointer = currPointer.next;
                nextPointer = currPointer.next;
            }
            else{
                currPointer.next = nextPointer;
            }
        }
        return head;
    }
}
