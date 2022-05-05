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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
	ListNode counter1 = l1;
	ListNode counter2 = l2;
	ListNode resultHead = new ListNode(0);
	ListNode resultPointer = resultHead;
	int sum = 0;
	while (counter1 != null || counter2 != null){
		sum /= 10;
		if(counter1 != null){
			sum += counter1.val;
			counter1 = counter1.next;
		}
		if(counter2 != null){
			sum += counter2.val;
			counter2 = counter2.next;
		}
		resultPointer.next = new ListNode(sum % 10);
		resultPointer = resultPointer.next;
	}
	if(sum / 10 == 1){
		resultPointer.next = new ListNode(1);
	}
	return resultHead.next;	
    }
}
