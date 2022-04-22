"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        #Copy the list without the randoms first
        newNode = self.nextRecursive(head)
        
        self.randomRecursive(head, newNode, head, newNode)
        return newNode
        
    def nextRecursive(self, head):
        if head:
            return Node(head.val, self.nextRecursive(head.next))
        else:
            return None

    def randomRecursive(self,head, newHead, copy, mod):
        if not copy:
            return
        if copy.random == None:
            self.randomRecursive(head, newHead, copy.next, mod.next)
        else:
            target = copy.random
            searchNode = head
            followNode = newHead
            while not searchNode == target:
                searchNode = searchNode.next
                followNode = followNode.next
            
            mod.random = followNode
            self.randomRecursive(head, newHead, copy.next, mod.next)