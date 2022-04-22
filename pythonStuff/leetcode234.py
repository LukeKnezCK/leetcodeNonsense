# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        backwards = [head]
        right = head.next
        while right.next:
            backwards.append(right)
            right = right.next
        left = head
        while not left == right and len(backwards) >= 1:
            if not left.val == right.val:
                return False
            left = left.next
            right = backwards.pop()
        return True