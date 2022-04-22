# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #base case
        if not head or head.next == None:
            return head
        
        #Split our list into two
        fastPointer = head.next.next
        slowPointer = head
        while fastPointer:
            fastPointer = fastPointer.next
            slowPointer = slowPointer.next
            if fastPointer:
                fastPointer = fastPointer.next
        leftHead = head
        rightHead = slowPointer.next 
        slowPointer.next = None
        
        #Recursively pass those two lists
        leftList = self.sortList(leftHead)
        rightList = self.sortList(rightHead)
        
        if rightList.val < leftList.val:
            newHead = rightList
            currentPointer = newHead
            rightList = rightList.next
        else:
            newHead = leftList
            currentPointer = newHead
            leftList = leftList.next
            
        while rightList and leftList:
            if rightList.val < leftList.val:
                currentPointer.next = rightList
                currentPointer = currentPointer.next
                rightList = rightList.next
            else:
                currentPointer.next = leftList
                currentPointer = currentPointer.next
                leftList = leftList.next
                
        while rightList:
            currentPointer.next = rightList
            currentPointer = currentPointer.next
            rightList = rightList.next
        while leftList:
            currentPointer.next = leftList
            currentPointer = currentPointer.next
            leftList = leftList.next
        
        return newHead
