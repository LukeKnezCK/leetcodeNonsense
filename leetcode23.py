# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        starter = ListNode(0,None)
        current = starter
        q = []
        for x in lists:
            q.append(x.value, x)
        q.sort()
        current.next = q[0]
        q.pop(0)
        current = current.next
        for y in q:
            current.next = q[y]
            current = current.next
        return starter