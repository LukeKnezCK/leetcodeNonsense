# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        trackedNodes = {head}
        nextNode = head.next
        while nextNode:
            if nextNode in trackedNodes:
                return True
            else:
                trackedNodes.add(nextNode)
                nextNode = nextNode.next
        return False