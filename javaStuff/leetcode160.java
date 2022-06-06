/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        Set<ListNode> encounters = new HashSet<>();
        ListNode pointerA = headA;
        ListNode pointerB = headB;
        while(pointerA != null){
            encounters.add(pointerA);
            pointerA = pointerA.next;
        }
        while(pointerB != null){
            if(!encounters.add(pointerB)) return pointerB;
            pointerB = pointerB.next;
        }
        return null;
    }
}
