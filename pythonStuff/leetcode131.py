class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] # which will be our answer
        self.helper(res, [], s) # calling to recursion function 
        return res
    
    # Entire recursive function, that generates all the partition substring
    def helper(self, res, curr, s):
        if s == "":
            res.append(curr)
        
        for i in range(len(s)):
            if self.isPalindrome(s[:i + 1]): # what we are checking over here is, if we partition the string from index to i Example-(0, 0) is palindrome or not
                self.helper(res, curr + [s[:i + 1]], s[i + 1:]) # take the substring and store it in our list & call the next substring from index + 1
    
    # A simple palindromic function start from 0 go till end. And basically keep on checking till they don't cross. 
    def isPalindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True

#Another solution i wrote before i realized that the function signature given was not condusive of recursion 
# class Solution:
#     def partition( s: str) -> list[list[str]]:
#         part = 1
#         totalList = []
#         while part < len(s):
#             currList = []
#             if Solution.palindrome(s[0:part]):
#                 currList.append(s[0:part])
#             currList.extend(Solution.partition(s[part:]))
#             part += 1
#             totalList.append(currList)
#         return totalList
            
        
#     def palindrome( s) -> bool:
#         leftPointer = 0
#         rightPointer = len(s)-1
#         while leftPointer < rightPointer:
#             if not s[leftPointer] == s[rightPointer]:
#                 return False
#             else:
#                 leftPointer += 1
#                 rightPointer -= 1
#         return True

#Something I wrote before figuring out what this poorly worded question actually wanted >:[
# class Solution:
    # def partition(self, s: str) -> list[list[str]]:
    #     counter = 0
    #     sList = list(s)
    #     totalList = []
    #     while counter < len(sList):
    #         leftPointer = 0
    #         rightPointer = counter
    #         currentList = []
    #         while rightPointer < len(sList):
    #             if Solution.palindrome(Solution, sList[leftPointer:rightPointer+1]):
    #                 currentList.append(str(sList[leftPointer:rightPointer+1]))
    #             leftPointer += 1
    #             rightPointer +=1
    #         counter += 1
    #         totalList.append(currentList)
    #     return totalList
        
    # def palindrome(self, s) -> bool:
    #     leftPointer = 0
    #     rightPointer = len(s)-1
    #     while leftPointer < rightPointer:
    #         if not s[leftPointer] == s[rightPointer]:
    #             return False
    #         else:
    #             leftPointer += 1
    #             rightPointer -= 1
    #     return True

Solution.partition( "aab")