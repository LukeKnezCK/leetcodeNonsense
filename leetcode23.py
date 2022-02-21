# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        starter = ListNode(0,None)
        current = starter
        q = PriorityQueue()
        for x in lists:
            if x:
                q.put((x.val, id(x), x))
        while not q.empty():
            current.next = q.get()[2]
            current = current.next
            if current.next: 
                q.put((current.next.val, id(current.next), current.next))
        return starter.next