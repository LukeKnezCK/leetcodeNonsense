import collections
#My solution which is too slow >:(
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        leftPointer = 0
        rightPointer = 0
        shortestSub = ""
        requiredLetters = collections.Counter(t)
        counter = collections.Counter()
        switcher = True
        while leftPointer < len(s):
            for x in requiredLetters.elements():
                if counter[x] < requiredLetters[x]:
                    switcher = True
                    break
                else:
                    switcher = False
            if not switcher:
                if len(shortestSub) > rightPointer-leftPointer or shortestSub == "":
                    shortestSub = s[leftPointer:rightPointer]
            if rightPointer <= len(s)-1 and switcher:                    
                counter[s[rightPointer]] += 1
                rightPointer += 1
            else:
                counter[s[leftPointer]] -= 1
                leftPointer += 1
        return shortestSub
                
#Another persons solution which is fast enough :p            
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_cnt = collections.Counter(t)
        i, j, found = 0, len(s)-1, 0
        min_win = ""
        for j in range(len(s)):
            if target_cnt[s[j]]>0:found += 1
            target_cnt[s[j]] -=1
            while found==len(t):
                #print(i, j, target_cnt)
                if not min_win or j-i+1<len(min_win):
                    min_win = s[i:j+1]
                target_cnt[s[i]]+=1
                if target_cnt[s[i]]>0:found -=1
                i+=1
        return min_win