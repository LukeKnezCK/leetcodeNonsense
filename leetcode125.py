import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = re.compile('[^a-zA-Z0-9]')
        
        stringList = list(regex.sub('',s).lower())
        leftPointer=0
        rightPointer = len(stringList)-1
        
        while leftPointer < rightPointer:
            if not stringList[leftPointer] == stringList[rightPointer]:
                return False
            leftPointer += 1
            rightPointer -= 1
        return True