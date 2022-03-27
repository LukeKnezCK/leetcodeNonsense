# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA and headB:
            return None
        encounteredNodes = set()
        pointerA = headA
        pointerB = headB
        while pointerA or pointerB:
            if pointerA in encounteredNodes: 
                return pointerA
            if pointerB in encounteredNodes:
                return pointerB
            if pointerA == pointerB:
                return pointerA
            if pointerA:
                encounteredNodes.add(pointerA)
                pointerA = pointerA.next
            if pointerB:
                encounteredNodes.add(pointerB)
                pointerB = pointerB.next
        return None