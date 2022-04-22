# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        newHead = self.reverseHelper(head, head.next)
        head.next = None
        return newHead
        
    def reverseHelper(self, last, curr):
        if curr.next == None:
            curr.next = last
            return curr
        head = self.reverseHelper(curr, curr.next)
        curr.next = last
        return head