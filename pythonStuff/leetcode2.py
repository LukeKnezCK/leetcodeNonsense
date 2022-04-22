# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = l1.val + l2.val
        if(l1.next == None and l2.next == None):
            if(sum > 10):
                sum = sum % 10
                return ListNode(sum, ListNode(1, None))
            elif(sum == 10):
                sum = 0
                return ListNode(sum, ListNode(1, None))
            else:
                return ListNode(sum, None)
            
        elif(l1.next == None):
            if(sum >= 10):
                sum = sum % 10
                return ListNode(sum, Solution.addTwoNumbers(self, ListNode(1,None), l2.next))
            elif(sum == 10):
                return ListNode(0, Solution.addTwoNumbers(self, ListNode(1,None), l2.next))
            else:
                return ListNode(sum, Solution.addTwoNumbers(self, ListNode(0,None), l2.next))
            
        elif(l2.next == None):
            if(sum >= 10):
                sum = sum % 10
                return ListNode(sum, Solution.addTwoNumbers(self, l1.next, ListNode(1,None)))
            elif(sum == 10):
                return ListNode(0, Solution.addTwoNumbers(self, l1.next, ListNode(1,None)))
            else:
                return ListNode(sum, Solution.addTwoNumbers(self, l1.next, ListNode(0,None)))
            
        if(sum >= 10):
            sum = sum % 10
            result = ListNode(sum, Solution.addTwoCarry(self, l1.next, l2.next))
            return result
        elif(sum == 10):
            sum = 0
            return ListNode(sum, Solution.addTwoCarry(self, l1.next, l2.next))
        else:
            nextNode = Solution.addTwoNumbers(self, l1.next, l2.next)
            result = ListNode(sum, nextNode)
            return result
    
    
    def addTwoCarry(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:   
        sum = l1.val + l2.val +1
        if(l1.next == None and l2.next == None):
            if(sum > 10):
                sum = sum % 10
                return ListNode(sum, ListNode(1, None))
            elif(sum == 10):
                sum = 0
                return ListNode(sum, ListNode(1, None))
            else:
                return ListNode(sum, None)
            
        elif(l1.next == None):
            if(sum >= 10):
                sum = sum % 10
                return ListNode(sum, Solution.addTwoNumbers(self, ListNode(1,None), l2.next))
            elif(sum == 10):
                return ListNode(0, Solution.addTwoNumbers(self, ListNode(1,None), l2.next))
            else:
                return ListNode(sum, Solution.addTwoNumbers(self, ListNode(0,None), l2.next))
            
        elif(l2.next == None):
            if(sum >= 10):
                sum = sum % 10
                return ListNode(sum, Solution.addTwoNumbers(self, l1.next, ListNode(1,None)))
            elif(sum == 10):
                return ListNode(0, Solution.addTwoNumbers(self, l1.next, ListNode(1,None)))
            else:
                return ListNode(sum, Solution.addTwoNumbers(self, l1.next, ListNode(0,None)))
            
        if(sum >= 10):
            sum = sum % 10
            result = ListNode(sum, Solution.addTwoCarry(self, l1.next, l2.next))
            return result
        elif(sum == 10):
            sum = 0
            return ListNode(sum, Solution.addTwoCarry(self, l1.next, l2.next))
        else:
            nextNode = Solution.addTwoNumbers(self, l1.next, l2.next)
            result = ListNode(sum, nextNode)
            return result